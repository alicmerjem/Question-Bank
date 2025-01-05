"""
When squirrels get together for a 
party, they like to have cigars. A 
squirrel party is successful when the
number of cigars is between 40 and 60
(inclusive). Unless it is the weekend,
in which case there is no upper bound 
on the number of cigars. Write a
function to return True if the party
given the value is successfull, or 
false otherwise. 
"""

def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >=40
    else:
        return 40 <= cigars <=60

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))
print(cigar_party(70, False))