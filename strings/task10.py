"""
write a function that removes the last
occurence of a given letter from a 
given string. if a given letter does not
appear in the string, then remove the
last and the first letter of the string.
"""

def remove_last_occurrence(lst, target):
    for i in range(len(lst) - 1, -1, -1):  # Iterate backwards
        if lst[i] == target:
            del lst[i]  # Remove the element
            break
    return lst