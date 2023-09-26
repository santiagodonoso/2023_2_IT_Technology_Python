from bottle import get, template
from _ import _db

##############################
@get("/")
def _():
  try:
    db = _db()
    return template("index")
  except Exception as e:
    return str(e)

##############################