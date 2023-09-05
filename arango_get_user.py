import requests

res = requests.get("http://127.0.0.1:8529/_api/document/users/128943", 
auth=("root", "password"))

print(res)








