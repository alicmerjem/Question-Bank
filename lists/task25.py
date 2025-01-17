"""
write a function to convert a list of 
multiple integers into a single int
"""
def list_to_int(lst):
    return int(''.join(map(str, lst)))

sample = [11, 33, 66]
print(list_to_int(sample))