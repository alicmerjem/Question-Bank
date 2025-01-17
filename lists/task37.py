"""
write a function to remove the kth
element from a given list, return
the new list
"""
def remove_the_kth(lst, k):
    return lst[:k] + lst[k+1:]

sample = [1, 1, 2, 3, 4, 4, 5, 1]
k = 2
print(remove_the_kth(sample, k))