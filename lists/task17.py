"""
write a function to select an item
randomly from a list
"""
import random
def select_rand(lst):
    return random.choice(lst)

list = [1, 2, 3, 4, 5]
print(select_rand(list))