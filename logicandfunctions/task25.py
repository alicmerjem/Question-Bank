"""
write a function to check whether a 
given integer is a palindrome or not
note: an integer is a palindrome
when it reads the same backward as
forwards. negative numbers cannot be
palindromes.
"""
def is_palindrome(num):
    return str(num) == str(num)[::-1]

print(is_palindrome(100))
print(is_palindrome(252))
print(is_palindrome(-838))