"""
We want to make a package of goal kilos
of choc. we have small bars (1kg each) 
and big bars (5kg each). return the num
of small bars to sum, assuming we
always use big bars before small bars.
write a function to return -1 if it 
cannot be done.
"""
def make_chocolate(small, big, goal):
    max_big = goal // 5
    if max_big > big:
        goal -= big * 5
    else:
        goal -= max_big * 5
    return goal if goal <= small else -1

print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))