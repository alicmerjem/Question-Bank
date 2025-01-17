"""
wrtie a function to pack consecutive
duplicates of a given list element
into sublists
"""

def pack_consecutive_duplicates(lst):
    result = []
    temp = []
    for i in range(len(lst)):
        if not temp or lst[i] == temp[-1]:
            temp.append(lst[i])
        else:
            result.append(temp)
            temp = [lst[i]]
    if temp:
        result.append(temp)
    return result

sample_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print(pack_consecutive_duplicates(sample_list))
