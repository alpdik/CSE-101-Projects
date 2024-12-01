def fib(n, check=False, x=0, a=0, b=1):
    if check==False:
        x=n
        check=True

    if n==0:
        return a
    if n==1:
        return b

    return fib(n-1,check,x,b,a+b)



print(fib(5))