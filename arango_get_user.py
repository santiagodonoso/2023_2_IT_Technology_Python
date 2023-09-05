import requests
import json

res = requests.get("http://127.0.0.1:8529/_api/document/users/128943", 
auth=("root", "password"))

# print(res) # <Response [200]>
# print(dir(res))

# print(type(res.content)) # <class 'bytes'>
# Convert the res to JSON
res = json.loads(res.content) # Convert res to JSON

# Show this in the teminal:
# Hi A Aa, your age is 1






