"""
write a function to find the 
appearance of the substring not and 
poor from a given string. if not 
follows poor, replace the whole not...poor
substring with good. return the resulting
string.
"""

def not_poor(s):
    not_index = s.find('not')
    poor_index = s.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return s[:not_index] + 'good' + s[poor_index + len('poor')]
    return s

print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))