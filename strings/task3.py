"""
write a function that for a given
string counts the number of words 
ending in y or z - so the y in heavy
and the z in fez count, but not the
y in yellow (not case sensitive).
we will say that a y or z is at the 
end of a word if there is no 
alphabetic letter immediatley
following it
"""
def countYZ(sentence):
    count = 0
    for word in sentence.split():
        if word[-1].lower() in ['y', 'z']:
            count+=1
        return count

print(countYZ("gray day thiz Monday"))
print(countYZ("gray day this Tuesday"))
print(countYZ("day fyyyz"))