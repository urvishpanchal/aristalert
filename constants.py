#!/usr/bin/python

# Syslog
fileName = "/opt/aristalert/Syslog.xlsx"

# Elasticserach 
severity = [0,0,0,0,0,0,0]
indices = "logstash-*"

errorStrings = ["%CAPACITY-1-UTILIZATION_HIGH",
                "%SAND-3-DDR_BIST_FAILED",
		"%SAND-3-INTERRUPT_OCCURRED",
		"%HARDWARE-3-ERROR_DETECTED",
                "%HARDWARE-3-DROP_COUNTER",
		"%HARDWARE-3-FPGA_PROGRAMMER_ERROR",
		"%HARDWARE-3-FPGA_CONFIG_ERROR",
#		"%TRANSCEIVER-4-AUTHENTICATION_FAILED",
                "%PROCMGR-4-TERMINATE_PROCESS_SIGQUIT",
                "%BGP-5-IF-MAXROUTESWARNING",
#                "PFC_WATCHDOG",
                "%SAND-4-FABRICSERDES_LINK_FAILED",
                "%FWK-3-SOCKET_CLOSE_LOCAL",
                "%HARDWARE-6-PERR_CORRECTED",
                "%PROGMGR-3-PROCESS_DELAYRESTART"]

changeSeverity = {"%SAND-3-INTERRUPT_OCCURRED":2,
		"%HARDWARE-3-ERROR_DETECTED":2,
		"%HARDWARE-3-DROP_COUNTER":2,
		"%SAND-3-DDR_BIST_FAILED":2,
		"%BGP-5-IF-MAXROUTESWARNING":2,
		"%PROGMGR-3-PROCESS_DELAYRESTART":2,
		"%CAPACITY-1-UTILIZATION_HIGH":2,
		"%SAND-4-FABRICSERDES_LINK_FAILED":2}


noSlackAlert = ["PowerSupplyDetector",
		"Xcvr",
		"Lm73",
		"Ucd9012",
		"Pmbus",
		"ApCaCertAgent",
		"Max6658",
		"SwanAgent"]

# Slack 
token = "xoxp-6379040466-6404165990-33235770069-05880a371b"      # found at https://api.slack.com/web#authentication
channel="#anetsyslogger"
username='slogbot'


# SMTP 
serverName = 'smtp.gmail.com'
serverPort = 587
serverLoginId = 'msft-alerts-ext@arista.com'
serverLoginPasswd = 'lsgipeqsjpdhsjiu'
fromAddr = "msft-alerts-ext@arista.com"
#toAddr = ["wasst@microsoft.com","msft-team@arista.com"]
toAddr = ["urvish@arista.com"]
