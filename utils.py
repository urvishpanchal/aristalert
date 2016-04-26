#!/usr/bin/python

from elasticsearch import Elasticsearch
import subprocess
from xlrd import open_workbook

def readXlsx(fileName):
	book = open_workbook(fileName)
	sheet = book.sheet_by_index(1)

	# read header values into the list    
	keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

	dict_list = []
	for row_index in xrange(1, sheet.nrows):
		d = {keys[col_index]: sheet.cell(row_index, col_index).value for col_index in xrange(sheet.ncols)}
		dict_list.append(d)

	#for row in dict_list:
	#	print row['Action']
	return dict_list


def searchElasticserach(indices, query, startTime, endTime):
	# Search the elasticsearch db.i
	es = Elasticsearch(timeout=600)
	res = es.search(index=indices,body={
	  "sort": [
	    {
	      "@timestamp": {
	        "order": "desc",
	        "unmapped_type": "boolean"
	      }
	    }
	  ],
	  "highlight": {
	    "pre_tags": [
	      "@kibana-highlighted-field@"
	    ],
	    "post_tags": [
	      "@/kibana-highlighted-field@"
	    ],
	    "fields": {
	      "*": {}
	    },
	    "fragment_size": 2147483647
	  },
	  "query": {
	    "filtered": {
	      "query": {
		"query_string": {
		  "query": query
		}
	      },
	      "filter": {
		"bool": {
		  "must": [
		    {
		      "range": {
			"@timestamp": {
			  "gte": startTime,
			  "lte": endTime
			}
		      }
		    }
		  ],
		  "must_not": []
		}
	      }
	    }
	  },
	  "size": 1000000,
	  "fields": [
	    "*",
	    "_source"
	  ],
	  "script_fields": {},
	  "fielddata_fields": [
	    "@timestamp"
	  ]
	}
	)
	return res['hits']['hits']


# This method adds or modifies the dictionary supplied
def modify(data,dictName):
	if isinstance(dictName, dict):
		if not data in dictName:
			dictName[data] = {'count':1}
		else:
			dictName[data]['count'] +=1
	return dictName

def createErrorDict(dictName,value):
	test[dictName] = value
	errorDict.update(test)

def getRegEx(dict_list):
	regEx = []
	for line in dict_list:
                regEx.append(line['Reg-Ex'])
	return regEx

def resultsPerHosts(res, hosts, dict_list):
	host = {}
	regEx = getRegEx(dict_list)
	for hit in res:
		host = modify(hit['_source']['host'],hosts)
		for i in  regEx:
			if i in hit['_source']['message']:
				#print "inside if"
				tmp = hit['_source']['host']
				host = modify(hit['_source']['message'],hosts[tmp])
	return host

def modifySeverity(res,severity,changeSeverity):
	for hit in res:
	       if hit['_source']['ar_tag'] in changeSeverity:
	               severity[changeSeverity[hit['_source']['ar_tag']]] += 1
	       else:
	               severity[hit['_source']['ar_severity']] += 1
	return severity
