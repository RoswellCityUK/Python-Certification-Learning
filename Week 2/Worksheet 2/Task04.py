"""
Program asks User for password (correct password = PASSWORD). The check is case-insensitive.
"""

user_password = input("Enter password: ")

if user_password.casefold() == "PASSWORD".casefold():
    print("Password is correct! Welcome.")
else:
    print("Password is incorrect! You are not welcome.")
