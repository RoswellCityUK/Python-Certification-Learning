"""
Program generates two list one with 10 odd number and second one with 10 even numbers
After that is generating one new list from both previous list in DESC order and print 3 first numbers
"""

newlist1 = [x for x in range(10*2) if x % 2 != 0]
print(newlist1, f"(len = {len(newlist1)})")

newlist2 = [x for x in range(10*2) if x % 2 == 0]
print(newlist2, f"(len = {len(newlist2)})")
print()

newlist3 = []
for x in range(len(newlist1)-1, -1, -1):
    newlist3.append(newlist1[x])
    newlist3.append(newlist2[x])

print(newlist3[:3])
