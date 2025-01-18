"""
write a function to convert a given
list of tuples to a list of lists
"""

def tuple_to_list(list_of_tups):
    list_of_lists = []
    for tup in list_of_tups:
        list_of_lists.append(list(tup))
    return list_of_lists