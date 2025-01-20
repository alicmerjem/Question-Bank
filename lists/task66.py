"""
write a function that for a given list
of strings returns a list where each
string has all its x removed
"""
def no_x(lst):
    result = []
    for s in list:
        result.append(s.replace('x', ''))
    return result

print(no_x(['ax', 'here is an x']))