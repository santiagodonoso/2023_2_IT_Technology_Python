import requests

url = "https://fiotext.com/send-sms"
myobj = {
  "user_api_key": "e13d1592688a13ae9aa0df5bd5fe554f",
  "sms_to_phone" : "YOUR_PHONE_NUMBER_HERE",
  "sms_message": "MESSAGE HERE"
  }

x = requests.post(url, data = myobj)

print(x.text)