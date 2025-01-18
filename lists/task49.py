"""
write a function to check whether a 
specified list is sorted or not
"""
def check_sort(lst):
    return lst == sorted(lst)

lst = [1, 2, 4, 6, 10, 3, 1]
print(check_sort(lst))