"""
Write a Python pattern to construct
the following pattern using a nested
for loop: 
    *
	* *
	* * *
	* * * *
	* * * * *
	* * * *
	* * *
	* *
	*
"""

rows = 5

# top half
for i in range (1, rows + 1):
    print("* " * i)

# bottom half
for i in range(rows - 1, 0, -1):
    print("* " * i)