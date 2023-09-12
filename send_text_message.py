import requests

url = "https://fiotext.com/send-sms"
myobj = {
  "user_api_key": "YOUR_API_KEY_HERE",
  "sms_to_phone" : "YOUR_PHONE_NUMBER_HERE",
  "sms_message": "MESSAGE HERE"
  }

x = requests.post(url, data = myobj) # data is "body form-data"

print(x.text)