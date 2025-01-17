"""
write a function to inser an element
before each element of a list
"""
def insert_b4(lst, element):
    result = []

    for item in lst:
        result.append(element)
        result.append(item)
    
    return result

sample = ['a', 'b', 'c', 'd']
element = 'x'
print(insert_b4(sample, element))