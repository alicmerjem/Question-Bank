"""
given 2 strings, a and b, write a 
function to reutrn a string of the 
form short + long + short, with the 
shorter string on the outside and 
the longer string on the inside. the
string will not be the same length, 
but they may be empty (len 0)
"""
def combo_string(s1, s2):
    if len(s1) < len(s2):
        short = s1
        long = s2
    else:
        short = s2
        long = s1
    
    return short + long + short

print(combo_string('Hello','hi'))
print(combo_string('hi','Hello'))
print(combo_string('aaa','b'))