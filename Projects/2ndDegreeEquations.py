import math
a=int(input("Enter the coefficient of x^2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the coefficient of 1: "))
disc=b**2-4*a*c
if disc<0:
    print("This function does not have a real root.")
    exit()

x1=(-b+math.sqrt(disc))/2*a
x2=(-b-math.sqrt(disc))/2*a


if x1!=x2:
    print(f"The first root of the function is equal to {x1}, the second root of th function is equal to {x2}")
elif x1==x2:
    print(f"The root of this function is {x1}")