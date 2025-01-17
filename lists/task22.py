"""
write a function to check whether a 
list contains a sublist
"""
def contains_sublist(lst, sublst):
    n = len(sublst)
    for i in range(len(lst) - n + 1):
        if lst[i:i+n] == sublst:
            return True
    return False

main = [1, 2, 3, 4, 5]
sub = [3, 4]
print(contains_sublist(main, sub))