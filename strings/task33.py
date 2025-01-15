"""
write a function to find the max len of
consecutive 0s in given binary string
"""

def function(s):
    zeros = s.split('1')
    return max(len(group) for group in zeros)

print(function('111000010000110'))
print(function('111000111'))