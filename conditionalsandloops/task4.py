"""
Write a Python program that takes two
digits m (row) and n (column) as input
and generates a two-dimensional array
the element value in the i-th row and
j-th colmn of the array should be i*j
"""

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

# creating a 2d array
array = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(i*j)
    array.append(row)

# displaying the array
for row in array:
    print(row)