"""
write a function to insert an element
in a given list after every nth position
"""

def insert_after_nth(lst, element, n):
    result = []
    for i in range(len(lst)):
        result.append(lst[i])

        if (i+1) % n == 0:
            result.append(element)
    return result

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(insert_after_nth(lst, 'a', 2))
print(insert_after_nth(lst, 'b', 4))