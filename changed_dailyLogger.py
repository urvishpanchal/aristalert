#!/usr/bin/python

import constants
import utils 

severity = [0,0,0,0,0,0,0]
hosts = {}

# Start time for the query. This is the time when the day started in milliseconds since epoch
startTime = int(datetime(today.year, today.month, today.day).strftime('%s'))*1000 

# End time for the query. This is the time when the day ends in milliseconds since epoch
endTime = int((datetime(today.year, today.month, today.day) + timedelta(1)).strftime('%s'))*1000 -1 

# filter for the query
query = "ar_severity: [0 TO 6] NOT (program: Lag+LacpAgent OR program: Thermostat OR program: Lldp OR program: Cli OR program: Ucd9012 OR program: PFC_WATCHDOG)"

result = utils.searchElasticserach(constants.indices, query, startTime, endTime)

#print json.dumps(res)
for hit in result:
	if hit['_source']['ar_tag'] in constants.changeSeverity:
		severity[changeSeverity[hit['_source']['ar_tag']]] += 1
	else:
		severity[hit['_source']['ar_severity']] += 1
	utils.modify(hit['_source']['host'],hosts)
	for i in  errorStrings:
		if i in hit['_source']['ar_tag']:
			tmp = hit['_source']['host']
			utils.modify(i,hosts[tmp])


# Create Log report file
f = open(fileName,'w+')
f.write("""From: %s
To: %s
MIME-Version: 1.0
Content-type:
Subject: %s


====TACBOT REPORT====

"""%(fromAddr, toAddr,emailSubject))
f.write("Sev 0 to 6 SYSLOG:\n")

#print "Got %d Sylogs grom %d unique devices" %(res['hits']['total'], len(hosts))
f.write("Got %d Sylogs grom %d unique devices\n" %(res['hits']['total'], len(hosts)))

# Print the Number of syslogs for each severity level per day
#print "\nSeverity:\n"
f.write("\nSeverity:\n")
for i in range(0,7):
	#print "severity %d cases = %d" %(i,severity[i])
	f.write("severity %d cases = %d\n" %(i,severity[i]))

# Print all the errors in the following format:
# Error Name:
# Host Name	Total Errors on that host per day 	Total errors of that kind per day
for error in errorStrings:
	#print "\n%s errors:\n" %(error)
	#f.write("\n%s errors:\n" %(error))
	flag = 0
	errorDict={}
	#sorted_list = {}
	#sorted_list = OrderedDict(sorted(hosts.iteritems(),key=lambda x: x[2][error]['value'], reverse=True))
	for k,v in hosts.iteritems():
		if error in v:
			#print "%s:\tTotal Errors:%d\tTotal %s Errors:%d" %(k,v['value'],error,v[error]['value'])
			#f.write("%s:\t%d\n" %(k,v[error]['value']))
			createErrorDict(k.lower(),v[error]['value'])
			flag=1
	if flag:
		f.write("\n%s Errors:\n" %(error))
		sorted_list = {}
		sorted_list = OrderedDict(sorted(errorDict.iteritems(),key=lambda x: x[1], reverse=True))
		i=0
		for k1,v1 in sorted_list.iteritems():
			f.write("%s:\t%d\n" %(k1,v1))
			i +=1
			if i==10:
				break
# Print the Host with the highest number of syslogs per day
# print "\nTop 10 Hosts:\n"
f.write("\nTop 10 Hosts:\n")

sorted_list = {}
sorted_list = OrderedDict(sorted(hosts.iteritems(),key=lambda x: x[1]['value'], reverse=True))
i = 0
for key,value in sorted_list.iteritems():
	#print "%s:%d"%(key,value['value'])
	f.write("%s:%d\n"%(key.lower(),value['value']))
	if i==9:
		break
	else:
		i +=1
f.close()
#print json.dumps(sorted_list)
#sendMail()

