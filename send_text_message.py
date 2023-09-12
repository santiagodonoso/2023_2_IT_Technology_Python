import requests
import json

url = "https://fiotext.com/send-sms"

with open("user_data.json", "r", encoding="utf-8") as my_file:
  # print(dir(my_file))
  # print(my_file.read())
  json_data = json.loads(my_file.read())
  print(type(json_data))
  mobile_number = json_data.get("user_mobile_number", "DEFAULT_NUMBER_HERE")
  # get the message from the file
  # get the api from the file
  
print(mobile_number)
# Do you remember context managers?
# Get the phone number from the file "user_data.json"
# Extract the number and replace it with "YOUR_PHONE_NUMBER_HERE"
# Note: The file is text, you must convert it to JSON - loads()
myobj = {
  "user_api_key": "YOUR_API_KEY_HERE",
  "sms_to_phone" : mobile_number,
  "sms_message": "MESSAGE HERE"
  }
x = requests.post(url, data = myobj) # data is "body form-data"
print(x.text)