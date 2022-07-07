"""
Program ask the User for login and password in a while(True) loop
The User has 3 attempts to provide valid credentials
otherwise the program will terminate.
"""
counter = 1

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "Admin" and password == "Password":
        print("Credentials correct! Welcome in the rabbit hole.")
        break
    elif counter == 3:
        print(f"Credentials incorrect! That was the final attempt. Fail to login.")
        break
    else:
        print(f"Credentials incorrect! Attempt {counter} out of 3. Try again. ")
    counter += 1
print("Program finished.")
