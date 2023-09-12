import requests
import json

# Documentation
# https://www.arangodb.com/docs/3.9/http/aql-query-cursor-query-results.html

q = {'query': 'FOR user IN users RETURN user'}
# res = requests.post("http://127.0.0.1:8529/_api/cursor", data=json.dumps(q), auth=("root", "password"))
res = requests.post("http://127.0.0.1:8529/_api/cursor", json=q, auth=("root", "password"))
# print(res.content)
users = json.loads(res.content)
print(users)
print(users.get("result")) # [{},{},{},{}]
for user in users.get("result"):
  # print(user)
  user_key = user.get("_key")
  res = requests.get(f"http://127.0.0.1:8529/_api/document/users/{user_key}", auth=("root", "password"))
  res = json.loads(res.content) # Convert res to JSON
  name = res.get('name')
  last_name = res.get('last_name')
  age = res.get('age')
  print(f"Hi {name} {last_name}, your age is {age}")


