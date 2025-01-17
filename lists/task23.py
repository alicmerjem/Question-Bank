"""
write a unction to create a list by
concatenating a given list which
range goes from 1 to n
"""
def create_list(list, n):
    result = []
    for i in range(1, n+1):
        for item in list:
            result.append(item + str(i))

    return result

sample = ['p', 'q']
n = 5

print(create_list(sample, n))