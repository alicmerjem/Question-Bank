"""
combine values in a list of 
dictionaries
"""
def combine_list_of_dicts(data):
    result = {}
    for item in data:
        for key, value in item.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result

# Sample Data
data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print(combine_list_of_dicts(data))
