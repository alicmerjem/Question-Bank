"""
write a function to compute the sum of
non zero groups (separated by zeros) 
of a given list of numbers
"""
def sum_groups(lst):
    sums = []
    current_sum = []
    for num in lst:
        if num != 0:
            current_sum += num
        else:
            if current_sum > 0:
                sums.append(current_sum)
    if current_sum > 0:
        sums.append(current_sum)

print(sum_groups([3, 4, 6, 2, 1, 0, 2, 4, 0, 0, 0, 7, 6, 5, 4]))