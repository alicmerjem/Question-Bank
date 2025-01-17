"""
write a function to split a given
list into two parts where the len
of the first part is given
"""

def split_list(lst, n):
    return lst[:n], lst[n:]

sample = [1, 1, 2, 3, 4, 4, 5, 1]
n = 3
print(split_list(sample, n))