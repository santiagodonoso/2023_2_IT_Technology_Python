# import validator
from validator import validate_username

while True:
  username = input("Enter username: ")
  if validate_username(username):
    with open("data.txt", "a") as my_file:
      my_file.write(username+"\n")
  else:
    print("invalid username")



