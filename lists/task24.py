"""
write a function to change the
position of every nth value with the 
(n+1)th in a list
"""
def swap_nth(lst):
    for i in range(0, len(lst) -1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    
    return lst

sample = [0, 1, 2, 3, 4, 5]
print(swap_nth(sample))