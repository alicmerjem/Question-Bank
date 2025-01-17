"""
write a function to insert a given string
at the beginning of all items in a 
list
"""
def insert_str(lst, string):
    return [string + str(item) for item in lst]

sample = [1, 2, 3, 4]
string = 'hehe'
print(insert_str(sample, string))