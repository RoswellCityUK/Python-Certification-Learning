"""
Task was to use try ... except ... block to handle errors in the program
"""

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lemonade"]

fifthLetter = []

try:
    for x in food:
        fifthLetter.append(x[4])
except IndexError:
    print("Some words have not enough letters to run the program")
except:
    print("An unknown signal from outer space caused the program to be violated")
