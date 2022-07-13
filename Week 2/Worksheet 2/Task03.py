"""
Program check if the provided product number contains "PRID" and gives User a feedback if the number
is correct and if it is in NEW ("PRID" on the beginning) or OLD format ("PRID" anywhere else).
"""

product_id = input("Enter product ID: ")

if product_id.count("PRID") == 0:
    print(product_id, "[Wrong]")
elif product_id.count("PRID", 1) > 0:
    print(product_id, "[OK - Old format]")
else:
    print(product_id, "[OK - New format]")
