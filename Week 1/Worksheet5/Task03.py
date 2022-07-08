"""
This piece of software is calculating factorial of a number using recursive function
"""


def calc_factorial(number):
    if number <= 1:
        return 1
    else:
        return number * calc_factorial(number-1)


print("0! =", calc_factorial(0))
print("1! =", calc_factorial(1))
print("3! =", calc_factorial(3))
print("5! =", calc_factorial(5))
