"""
write a function to check if a given
element occurs at least n times in a 
list
"""
def occurs_n_times(lst, element, n):
    return lst.count(element) >= n

lst = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
print(occurs_n_times(lst, 3, 4))
print(occurs_n_times(lst, 0, 5))
print(occurs_n_times(lst, 8, 3))