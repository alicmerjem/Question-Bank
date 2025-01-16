"""
write a python function to print a 
specified list after removing the 0th,
4th and 5th elements
"""
def remove_elements(lst):
    result = []
    for i in range(len(lst)):
        if i not in [0, 4, 5]:
            result.append(lst[i])
    return result

sample = ['red', 'green', 'white', 'black', 'pink', 'yellow']
print(remove_elements(sample))