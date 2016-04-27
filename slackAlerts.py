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
	startTime= int(time.time()*1000) -600000

	# End time for the query. This is end of the day time
	endTime= int(time.time()*1000)

	#print query
	query = "_exists_ : ar_tag"

	result = utils.searchElasticserach(constants.indices, query, startTime, endTime)

	errors = utils.readXlsx(constants.fileName)

	hosts = {}
	hosts = utils.resultsPerHosts(result, hosts, errors)

	#print hosts

	regEx = utils.getRegEx(errors)
	message = ""
	for hostname,v in hosts.iteritems():
	#	print k, v
		message = ""
		for string in regEx:
	#		print string
			if string.strip() in str(v):
				#test = str(v).split(',')
				#print test
				#print v['count']
				for key,value in v.iteritems():
					if isinstance(value, dict):
						for count, number in value.iteritems():
							#print key, messageCount
							if not any(agent in str(key) for agent in constants.noSlackAlert):
								message = message + "\nMessage : " + str(key) +  " Count: " + str(number)
							#output.sendSlackAlert(constants.token, constants.channel, constants.username, "Message : " + str(key), " Count: " + str(number))
					else:
						#print key , value
						message = "Host: " + str(hostname) + " Count: " + str(value)
						#output.sendSlackAlert(constants.token, constants.channel, constants.username, "Host: " + str(hostname), " Count: " + str(value))
		if message:
			#print message + "\n"
			output.sendSlackAlert(constants.token, constants.channel, constants.username, message)
	#for error in constants.errorStrings:
	#	for k,v in hosts.iteritems():
	#		if error in str(v):
	#			output.sendSlackAlert(constants.token, constants.channel, constants.username, k, error, v[error]['value'])
				#sc.api_call(
				#	"chat.postMessage", channel="#anetsyslogger", text="Host: "+ k + "\nError: " + error + "\nCount: " + str(v[error]['value']),
				#	username='slogbot'
				#)


if __name__ == '__main__':
  main()
