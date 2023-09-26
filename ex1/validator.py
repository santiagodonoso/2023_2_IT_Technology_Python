import re

regex_username = "^[a-z0-9_]{2,20}$"

def validate_username(the_name):
  return re.match(regex_username, the_name)



