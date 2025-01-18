"""
write a function to convert a tuple 
of string values to a tuple of
integer values
"""

def convert_to_int(tup):
    new_tuple = []
    for inner in tup:
        new_inner = []
        for value in inner:
            new_inner.append(int(value))
        new_tuple.append(tuple(new_inner))

    return tuple(new_tuple)

print(convert_to_int((('333', '33'), ('1416', '55'))))
