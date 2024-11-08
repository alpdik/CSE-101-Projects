import math
def trig(a,b):
    c=math.sqrt(a**2+b**2)
    return c

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print("The hypotenuse of the trianglle is:", trig(a, b))