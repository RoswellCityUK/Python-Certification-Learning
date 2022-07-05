"""
Title: Minutes to Seconds calculator
Author: Tomasz Grabowski
05/07/2022
"""

seconds = float(input("Enter a number of seconds: "))  # Asks User to enter number of seconds
minutes = seconds / 60  # Calculates number of minutes
print("{0:g}".format(seconds), "seconds =", "{0:g}".format(minutes), "minutes")  # Outputs data
