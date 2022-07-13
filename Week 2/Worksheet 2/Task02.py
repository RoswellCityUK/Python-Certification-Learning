"""
Program ask for student number and last name. Program should check that student number contains only numbers
and last name contains only letters
"""
error_flags = 0b00

student_number = input("Enter student number: ")
student_lastname = input("Enter last name: ")

if not student_number.isnumeric():
    error_flags |= 0b01
if not student_lastname.isalpha():
    error_flags |= 0b10

if error_flags == 0b11:
    print("Input invalid")
elif error_flags == 0b01:
    print("Invalid Student Number")
elif error_flags == 0b10:
    print("Invalid Last Name")
else:
    print("Input Verified")
