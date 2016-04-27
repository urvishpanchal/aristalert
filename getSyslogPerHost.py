#!/usr/bin/python

from datetime import datetime,timedelta
import time
import utils
import constants
import output
import itertools

def main():

        today = datetime.utcnow().date()

        #print startTime
        startTime= 1461250800000 

        # End time for the query. This is end of the day time
        endTime= 1461258000000

        #print query
        hosts = ['"co3sch01020aalf"',
'"co3sch01020bblf"',
'"co3sch01021aalf"',
'"co3sch01021bblf"',
'"co3sch01022aalf"',
'"co3sch01022bblf"',
'"co3sch01023aalf"',
'"co3sch01023bblf"',
'"co3sch01024aalf"',
'"co3sch01024bblf"',
'"co3sch01025aalf"',
'"co3sch01025bblf"',
'"co3sch01026aalf"',
'"co3sch01026bblf"',
'"co3sch01027aalf"',
'"co3sch01027bblf"',
'"co3sch01028aalf"',
'"co3sch01028bblf"',
'"co3sch01029aalf"',
'"co3sch01029bblf"']

        for host in hosts:
		result = utils.searchElasticserach(constants.indices, host, startTime, endTime)
		print host	
		for hit in result:
			print hit['_source']['@timestamp'] + "\t" + hit['_source']['ar_tag'] +"\t" +hit['_source']['message']
			
		print "\n"

if __name__ == '__main__':
	main()
