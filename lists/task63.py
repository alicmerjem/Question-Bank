"""
write a function to count the number
of groups of non zero numbers separated
by zeros of a given list of numbers
"""
def count_groups(lst):
    count = 0
    in_group = False
    for num in lst:
        if num!=0:
            if not in_group:
                count+=1
                in_group = True
        else:
            in_group = False
    return count

print(count_groups([3, 4, 6, 2, 0, 0, 0, 0, 7, 6, 2, 0, 0, 0]))