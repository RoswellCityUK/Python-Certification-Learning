"""
Target here was to add Exception handling to the provided code
"""

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lemonade"]

fifthLetter = []

for x in food:
    try:
        fifthLetter.append(x[4])
    except IndexError:
        print("A word less than 5 characters long was encountered")

print(fifthLetter)
