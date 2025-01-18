"""
write a fnction to count the integers 
in a given mixed list
"""
def count_integers(lst):
    return sum(1 for item in lst if isinstance(item, int))

lst = [1, 'abc', 3, 1.15, 'hehe', -5, 'something goes here']
print(count_integers(lst))
