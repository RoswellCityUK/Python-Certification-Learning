"""
Program should include function which analyse the provided number [int: 1-10].
    - If number is outside the range -> raise ArithmeticError and re-raise after handling in function
    - If string is provided -> ValueError and handled only in caller
    - If no exceptions -> print "Everything is beautiful."
Program should end with "End of code" regardless of the exceptions.
"""


def analyse(number):
    try:
        number = float(number)
        if number < 0 or number > 10:
            raise ArithmeticError('Error: Number outside the range')
    except ArithmeticError:
        print("ArithmeticError handled in function")
        raise


user_number = input("Enter number: ")

try:
    analyse(user_number)
except ValueError:
    print('ValueError handled by caller')
except ArithmeticError:
    print('ArithmeticError re-handled by caller')
else:
    print('Everything is beautiful.')
print('End of code.')
