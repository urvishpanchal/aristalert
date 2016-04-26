import time
from slackclient import SlackClient
import urllib3
urllib3.disable_warnings()

token = "xoxp-6379040466-6404165990-33235770069-05880a371b"      # found at https://api.slack.com/web#authentication
sc = SlackClient(token)
#print sc.api_call("api.test")
#print sc.api_call("channels.info", channel="#general")
hello="hello"
sc.api_call(
    "chat.postMessage", channel="#general", text="test" + hello,
    username='slogbot', icon_emoji=':robot_face:'
)
