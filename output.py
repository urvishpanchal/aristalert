#!/usr/bin/python

import smtplib
from slackclient import SlackClient
import urllib3
urllib3.disable_warnings()

def sendSlackAlert(token, channel, username, *args):
	sc = SlackClient(token)
	sc.api_call(
		"chat.postMessage", 
		channel=str(channel), 
		text=args[0] + "\n",
		username=str(username))

def sendMail(serverName, serverPort, serverLoginId, serverLoginPasswd, fileName,fromAddr, toAddr):
        server = smtplib.SMTP(serverName, serverPort)
        server.ehlo()
        server.starttls()
        server.login(serverLoginId, serverLoginPasswd)
        with open(fileName,'r') as content_file:
                message = content_file.read()
        server.sendmail(fromAddr, toAddr, message)
