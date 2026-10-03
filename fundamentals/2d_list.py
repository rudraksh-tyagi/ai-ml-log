l = [[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]]

# print(l[2][2])  # Output: 9

for row in l:
    for element in row:
        print(element)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9

l2 = [[]]

x = int(input("Enter the number of rows: "))
y = int(input("Enter the number of columns: "))

for i in range(x):
    row = []
    for j in range(y):
        value = int(input(f"Enter value for row {i+1}, column {j+1}: "))
        row.append(value)
    l2.append(row)

print("The 2D list you entered is:")
for row in l2:
    print(row)