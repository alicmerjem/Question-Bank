"""
write a function to find the next 
smallest palindrome of a specified number
"""
def next_smallest_palindrome(num):
    num+= 1
    while str(num) != str(num)[::-1]:
        num+=1
    return num

print(next_smallest_palindrome(99))
print(next_smallest_palindrome(1221))