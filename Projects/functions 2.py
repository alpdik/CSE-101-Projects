#is it a triangle?
def is_triangle(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False
#area of the triangle
def area(a, b, c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return area
#perimeter of the triangle
def perimeter(a, b, c):
    return a+b+c
#triangle type
def triangle_type(a, b, c):
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        return "right angled"
    elif a**2+b**2>c**2 or a**2+c**2>b**2 or b**2+c**2>a**2:
        return "acute angled"
    else:
        return "obtuse angled"
#main function
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))
if is_triangle(a, b, c):
    print("The triangle is valid.")
    print("The area of the triangle is:", area(a, b, c))
    print("The perimeter of the triangle is:", perimeter(a, b, c))
    print("The triangle is a", triangle_type(a, b, c), "triangle.")
else:
    print("The triangle is not valid.")
