"""
Give to 2 ints, a and b, and return
their sum. However, sums in the range
10..19 inclusive are forbidden, so
in that case just return 20.
"""

def sorta_sum(a, b):
    total = a + b
    if 10 <= total <= 19:
        return 20
    return total

print(sorta_sum(3, 4))   # → 7 (sum is 7, which is allowed)
print(sorta_sum(9, 4))   # → 20 (sum is 13, which is within the forbidden range)
print(sorta_sum(10, 11)) # → 21 (sum is 21, which is allowed)
