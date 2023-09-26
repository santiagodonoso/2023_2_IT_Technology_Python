import requests

##############################
def _db():
  url = 'http://127.0.0.1:8529'
  myobj = {'ping': 'pong'}
  db = requests.post(url, myobj)
  print("xxxxxxxxxxxxxxxxx", db.status_code)
  print("xxxxxxxxxxxxxxxxx", type(db.status_code))
  if db.status_code is not 200: raise Exception("db error")
  return db




















