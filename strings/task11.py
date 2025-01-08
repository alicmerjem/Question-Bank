"""
given two strings a and b, write a 
function to return the result of
putting them together in the order abba
e.g. hi and bye = hibyebyehi
"""
def makeabba(s1, s2):
    return s1+s2+s2+s1


print(makeabba('hi', 'bye'))
print(makeabba('yo', 'alice'))
print(makeabba('what', 'up'))