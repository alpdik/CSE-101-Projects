import math
a=int(input("input the 1st side of the triangle: "))
b=int(input("input the 2nd side of the triangle: "))
deg=int(input("Input the degree between the two sides: "))
if 0<deg<180:
    c=math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(deg)))
    print(c)
else:
    print("Enter a valid triangle")