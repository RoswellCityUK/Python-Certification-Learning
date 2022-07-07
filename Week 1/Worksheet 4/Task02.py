"""
Program prints out first 10 odd numbers
"""
newlist = [x for x in range(10*2) if x % 2 != 0]
print(newlist, f"(len = {len(newlist)})")
