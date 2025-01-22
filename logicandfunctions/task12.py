"""
We want to make a row of bricks that is
an inch long. We have a number of small
bricks (1 inch ling) and big bricks
(5 inches ling). Return true if it is
possible to make the goal by choosing
from the given bricks. 
"""

def make_bricks(small, big, goal):
    max_big = goal // 5
    if max_big > big:
        goal -= big * 5
    else:
        goal -= max_big * 5
    return goal <= small

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))
