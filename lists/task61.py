"""
write a function to convert a given
decimal number to binary list
"""
def decimal_to_binary(n):
    binary = []
    while n > 0:
        binary.insert(0, n%2)
        n = n // 2
    
    return binary

print(decimal_to_binary(8))
print(decimal_to_binary(45))
print(decimal_to_binary(100))