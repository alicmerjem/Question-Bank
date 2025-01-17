"""
write a function to remove consecutive 
duplicated of a given list
"""

def remove_dup(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]

sample = [0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5]
print(remove_dup(sample))