"""
write a function to check if a 
specified element presents in a tuple
of tuples
"""
def check_element_in_tuple(tup_of_tups, element):
    for tup in tup_of_tups:
        for value in tup:
            if value == element:
                return True
            
    return False

print(check_element_in_tuple((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), 'White'))