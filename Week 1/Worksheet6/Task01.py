"""
Simple program to iterate through the dictionary and prints out some phrases based on dictionary content
"""

mathconstants = {"pi": 3.14, "e": 2.72, "g": 9.81, "root2": 1.41}

for key in mathconstants.keys():
    print(f"The value associated with {key} is {mathconstants[key]}.")
