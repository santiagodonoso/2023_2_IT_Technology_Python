import re

"""
Create a program that allows a user 
to enter a username.
The username is validate via a regex
The regex is inside another file called
'validator.py'
The user enters the username and it gets 
validated
if the username is correct, it is saved
in a file (appended to the file) context manager
If the user is incorrect, try again
It runs until you kill the program (ctr+c)
"""









# Create a regex for a username
# The name can be 2 to 20 letters (capital or lower case), 
# numbers or underscores
regex_username = "^[a-zA-Z0-9_]{2,20}$"
username = "[a34_bc1_[23_]]"
if re.match(regex_username, username):
  print("valid username")
else:
  print("invalid username")


# Create a regex for a first name
# The name can be 2 to 20 letters
# The first letter must be capitalized
# all other 19 letters lowered cased
# regex_first_name = "^[A-Z][a-z]{1,19}$"


# Create a regex for a first name
# The name can be 2 to 20 letters
# It can contain lower case and upper case letters
# regex_first_name = "^[A-z]{2,20}$"


"""
phone = "12345678"
regex_phone = "^[1-9][0-9]{7}$"
if re.match(regex_phone, phone):
  print("valid phone")
else:
  print("invalida phone")
"""





# must have 3 letters
# regex_name = "^[a-z]{3}$" 

# at least 2 letters, no max limit
# regex_name = "^[a-z]{2,}$" 

# 2 to 20 letters
# regex_name = "^[a-z]{2,5}$" 

# name = "abcdef"
# if re.match(regex_name, name):
#   print("valid name")
# else:
#   print("invalid name")
