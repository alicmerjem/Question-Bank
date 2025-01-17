"""
write a function to extract a given
number of randomly selected elements
from a given list
"""
import random

def extract_random(lst, number):
    return random.sample(lst, number)

sample = [1, 1, 2, 3, 4, 4, 5, 1]
number = 3
print(extract_random(sample, number))