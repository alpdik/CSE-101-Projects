def gcd(x,y):
    if x%y==0:
        if x>y:
            return y
        else:
            return x
    else:
        if x>y:
            return gcd(y,x%y)
        else:
            return gcd(x,y%x)

print(gcd(345345,345))