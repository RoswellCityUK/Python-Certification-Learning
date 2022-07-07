"""
Program generates 2D Matrix where value of a cell is equal to square of the column number
After that prints out [1,1], [2,2] and [3,3] elements
"""

x_list = []
for x in range(3):
    x_list.append([])
    for y in range(3):
        x_list[x].append((y+1) ** 2)

print("Generated matrix: ", x_list)

for element in range(len(x_list)):
    print(f"[{element}, {element}] = ", x_list[element][element])
