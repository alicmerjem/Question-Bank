"""
write a function to concatenate three 
dictionaries to create a new one
"""
def concatenate_dicts(dic1, dic2, dic3):
    return {**dic1, **dic2, **dic3}

dic1 = {1:10, 2:20}
dic2 = {3: 30, 4:40}
dic3 = {5:50, 6:60}
result = concatenate_dicts(dic1, dic2, dic3)
print(result)