# The name inputed by the user must be inside
# a dictionary
# The dictionary is inside a list
# When you remove 1 or many names that are
# equal, all those dictionaries get deleted

# []
# {"name":"c"}
# [{"name":"a"}, {"name":"b"}, {"name":"c"}, {"name":"a"}]
# [ {"name":"b"}, {"name":"c"} ]
#

people = [] # many
person = {"name":"a", "last_name":"aa"} # one
people.append(person)


# newlist = [x for name in names if "a" in name]
# ["lasse", "santiago"]

people = []
while True:
  option = input("1. Enter name   2. Delete name   3.Show people  *. Exit\n")
  if option == "1":
    name = input("Enter name:")
    person = {"name":name}
    people.append(person)
    print(people)
  elif option == "2":
    delete_name = input("Enter name to be deleted:")
    for person in people:
      if person["name"] == delete_name:
        print("removing person...")
        people.remove(person)
      print(person)
  elif option == "3":
    print(people)
  else:
    break




"""
name = "a"
last_name = "aa"

person = {
    "name": name,
    "last_name": last_name
}

print(person)
"""



"""
names = []
while True:
  option = input("1. Enter name   2. Delete name   3.Show names  *. Exit")
  if option == "1":
    name = input("Enter name:")
    names.append(name)
    print(names)
  elif option == "2":
    delete_name = input("Enter name to be deleted:")
    for i in names:
      if delete_name in names: 
        names.remove(delete_name)
  elif option == "3":
    print(names)
  else:
    break
"""

"""  
  #print(names)
  for i in names:
    print(i)
    if delete_name in names:
      names.remove(delete_name)
  print(names)
"""


"""
Create a system that does:
A user can enter many names
A user can choose to delete a name, based
on the name itself
A user can choose to exit the system
The names entered are saved in a list

1) To enter a name 2) To delete a name 3) exit
Enter name: A

1) To enter a name 2) To delete a name 3) exit 
Enter name: B

1) To enter a name 2) To delete a name 3) exit
Enter name to delete: A

1) To enter a name 2) To delete a name 3) exit
Enter name to delete: B

1) To enter a name 2) To delete a name 3) exit 4) Show names


"""






"""
Input from a user
add data to a list
delete data from a list
loop through a list
"""




"""
names = ["a", "b", "c"]
for i in names:
    print(i)
"""






"""
while True:
    name = input("Name:")
    if name == "exit" : break
""" 










"""
name = input("Name:")
last_name = input("Last name:")
print(f"Hi {name} {last_name}")
"""









"""
# Get the user' name from the terminal
# Add the name to a list of names
# Show the name entered by the user "Hi xxxxx"
names = []
name = input("Enter your name:")
# TODO: Add the name to a list of names
names.append(name)
print(f"Hi {name}")
print(names)

# Prompt the user to enter the name
# Prompt the user to enter the last name
# Hi A B
"""










"""
prices = [1,2,3]
print(prices[0])
# Delete number 2 from the list
del prices[2]
# prices = [1,3]
# Print the whole list
# [1,3]
print(prices)
"""






"""
year = 2023
price = 10
10.99 * 100 = 1099
1099 / 100 = 10.99
"""
