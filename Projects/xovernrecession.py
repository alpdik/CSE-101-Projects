def x_tttpo_n(x, n):
    if n==0:
        return 1
    if n==1:
        return x

    return x*x_tttpo_n(x,n-1)

print(x_tttpo_n(2,3))