"""
write a function to find the largest
and smallest digit in a given number
"""
def largest_smallest_digit(num):
    digits = [int(digit) for digit in str(num)]
    return f"Largest: {max(digits)}, Smallest: {min(digits)}"

print(largest_smallest_digit(9387422))