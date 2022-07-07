"""
The software checks if the User has entered a leap year or a common year.
"""

user_year = int(input("Enter YEAR to check: "))

if user_year % 4 == 0:
    if user_year % 100 == 0 and user_year % 400 != 0:
        print(f"{user_year} is a common year.")
    else:
        print(f"{user_year} is a leap year.")
else:
    print(f"{user_year} is a common year.")
