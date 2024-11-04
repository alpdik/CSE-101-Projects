number=int(input("Enter a number:"))
y=int(1)
z=int(0)
for x in range(1,number+1):
    while x>0:
        y*=x
        x-=1
    z+=y
    y=int(1)
print("Your sum of factorials is:", z)