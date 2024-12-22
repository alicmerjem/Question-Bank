"""
Write a Python program that checks if
a triangle is equilateral,
isosceles or scalene:
1) equilateral all 3 sides equal
2) scalene 3 unequal sides
3) isosceles at least 2 equal strokes
"""

def triangle_type(a, b, c):
    if a==b==c:
        return "Equilateral"
    if a==b or b==c or a==c:
        return "Isosceles"
    else:
        return "Scalene"
    
side1 = float(input("Enter the length of side one: "))
side2 = float(input("Enter the length of side two: "))
side3 = float(input("Enter the length of side three: "))

# ensure all the sides are valid
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    result = triangle_type(side1, side2, side3)
    print("The triangle is: ", result)
else:
    print("The entered sides do not form a valid triangle.")