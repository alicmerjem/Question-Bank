"""
write a function to count the frequency
of consecutive duplicate elements in a
given list of numbers
"""
def consecutive_frq(lst):
    unique = []
    counts = []

    for num in lst:
        if unique and num == unique[-1]:
            counts[-1] += 1
        else:
            unique.append(num)
            counts.append(1)
    return unique, counts

lst = [1, 2, 2, 2, 2, 4, 4, 4, 5, 5]
print(consecutive_frq(lst))
