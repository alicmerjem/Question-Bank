"""
For this problem we will round an int
value up to the next multiple of 10
if its rightmost digit is 5 or more,
so 15 rounds up to 20. alternatively,
round down to the previous multiple
of 10 if its rightmost digit is less
than 5, so 12 rounds down to 10. Write
a function that gives 3 ints, returns
the sum of their rounded values.
"""
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    return (num+5)// 10*10

print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))