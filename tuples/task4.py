"""
write a function to convert a tuple
of positive integers into an integer
"""

def tuple_to_integer(tup):
    num_str = ''
    for num in tup:
        num_str += str(num)
    return int(num_str)

print(tuple_to_integer((1, 2, 3)))