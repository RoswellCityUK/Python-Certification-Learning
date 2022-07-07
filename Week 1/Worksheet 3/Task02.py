"""
Program is asking User to enter his name and integer number
then print this name given number of times using While and For loops
"""

user_name = input("Enter your name: ")
user_number = int(input("Enter integer number: "))

counter = 0

print()
print("Printing name with while loop:")
while counter < user_number:
    print(user_name, end=" ")
    counter += 1
print("\n")
print("Printing name with for loop")
for x in range(user_number):
    print(user_name, end=" ")
print()
