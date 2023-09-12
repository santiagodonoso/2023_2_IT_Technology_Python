import requests

url = "https://fiotext.com/send-sms"

# Do you remember context managers?
# Get the phone number from the file "user_data.json"
# Extract the number and replace it with "YOUR_PHONE_NUMBER_HERE"
# Note: The file is text, you must convert it to JSON - loads()
myobj = {
  "user_api_key": "YOUR_API_KEY_HERE",
  "sms_to_phone" : "YOUR_PHONE_NUMBER_HERE",
  "sms_message": "MESSAGE HERE"
  }

x = requests.post(url, data = myobj) # data is "body form-data"

print(x.text)