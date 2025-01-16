"""
write a function to count the number of
strings where the string length is 2 or
more and the first and last character 
are the same from a given list of 
string
"""
def count_strings(lst):
    count = 0
    for string in lst:
        if len(string)>=2 and string[0] == string[-1]:
            count += 1
    return count

sample = ['abc', 'xyz', 'aba', '1221']
print(count_strings(sample))