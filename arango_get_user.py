import requests
import json

# Get the _key for user A and B
users_keys = ["128943", "129057"]
for key in users_keys:
  res = requests.get(f"http://127.0.0.1:8529/_api/document/users/{key}", auth=("root", "password"))
  res = json.loads(res.content) # Convert res to JSON
  name = res.get('name')
  last_name = res.get('last_name')
  age = res.get('age')
  print(f"Hi {name} {last_name}, your age is {age}")



"""
# Exercise:
# Create a program that shows both users
# Hi A Aa, your age is 1
# Hi B Bb, your age is 2

res = requests.get("http://127.0.0.1:8529/_api/document/users/128943", 
auth=("root", "password"))

# print(res) # <Response [200]>
# print(dir(res))

# print(type(res.content)) # <class 'bytes'>
# Convert the res to JSON
res = json.loads(res.content) # Convert res to JSON
# Show this in the teminal:
# Hi A Aa, your age is 1
name = res.get('name')
last_name = res.get('last_name')
age = res.get('age')
print(f"Hi {name} {last_name}, your age is {age}")
"""





