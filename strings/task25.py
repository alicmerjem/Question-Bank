"""
write a function to return true if the 
given string contains an appearance of
xyz where the xyz is not directly
preceeded by a period
e.g xxyz counts but x.xyz does not
"""
def xyz_there(s):
    for i in range(1, len(s)-2):
        if s[i:i+3] == 'xyz' and s[i-1] != '.':
            return True
    
    if s[:3] == 'xyz':
        return True
    return False

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))