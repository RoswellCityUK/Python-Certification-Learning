"""
String manipulation: Program ask for User firstname and lastname, then prints out lastname followed
by their first initial separated by comma.
"""

user_fullname = input("Enter your firstname and lastname: ")

user_fullname = user_fullname.split(" ")
user_firstname = user_fullname[0].capitalize()
user_lastname = user_fullname[-1].capitalize()

print("User name: ", user_lastname + "." + user_firstname[0])
