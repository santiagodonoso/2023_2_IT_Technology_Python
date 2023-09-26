import re

# must have 3 letters
# regex_name = "^[a-z]{3}$" 

# at least 2 letters, no max limit
# regex_name = "^[a-z]{2,}$" 

# 2 to 20 letters
# regex_name = "^[a-z]{2,5}$" 

name = "abcdef"
if re.match(regex_name, name):
  print("valid name")
else:
  print("invalid name")
