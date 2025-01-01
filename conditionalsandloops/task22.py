"""
Write a program that checks whether
a triangle is right angled triangle
right angled - if we can apply the 
pythagorean theorem
"""

def is_right_angled_triangle(a, b, c):
    hypothenuse = max(a, b, c)

    sides = [a, b, c]
    sides.remove(hypothenuse)
    leg1, leg2 = sides[0], sides[1]

    return hypothenuse**2 == leg1**2 + leg2**2

a = float(input("Enter the first side of the tirangle: "))
b= float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

if is_right_angled_triangle(a, b, c):
    print("The triangle is a right-angled triangle.")
else:
    print('The triangle is not a right-angled triangle.')

