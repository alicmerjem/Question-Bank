"""
write a python function to count the
number of elements in a list within
a specified range
"""
def count_in_rnage(lst, start, end):
    count = 0
    for num in lst:
        if start <= num <= end:
            count += 1
    return count

sample = [10, 20, 30, 40, 50]
start = 20
end = 50

print(count_in_rnage(sample, start, end))