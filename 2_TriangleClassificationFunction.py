def classify_triangle(a, b, c):
    # Validate numeric input
    if not all(isinstance(side, (int, float)) for side in (a, b, c)):
        return "Invalid input: All sides must be numbers."

    # Check for zero or negative values
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle: Sides must be positive numbers."

    # Triangle Inequality Theorem check
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle: Triangle inequality violated."

    # Classification
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
    

print(classify_triangle(3, 3, 3))
print(classify_triangle(5, 5, 3))
print(classify_triangle(4, 5, 6))
print(classify_triangle(1, 2, 3))
print(classify_triangle(0, 4, 5))  

