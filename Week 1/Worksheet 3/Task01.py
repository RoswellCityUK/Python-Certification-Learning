"""
User provides 3 different number and program is
looking for max and min value with only if statements
"""

print("Enter 3 different numbers: ")
x1 = float(input("x1 = "))
xmin = x1
xmax = x1

x2 = float(input("x2 = "))
if x2 < xmin:
    xmin = x2
elif x2 > xmax:
    xmax = x2

x3 = float(input("x3 = "))
if x3 < xmin:
    xmin = x3
elif x3 > xmax:
    xmax = x3

print(f"The biggest provided number is: {xmax:g}")
print(f"the smallest provided number is: {xmin:g}")
