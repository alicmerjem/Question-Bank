"""
write a function to compute the sum
of all elements of each tuple stored
inside a list of tuples
"""

def sum_of_elements_in_tuples(list_of_tups):
    sums = []
    for tup in list_of_tups:
        total = 0
        for num in tup:
            total += num
        sums.append(total)
    return sums
