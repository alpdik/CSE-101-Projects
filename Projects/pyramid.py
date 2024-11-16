def chrismas_tree():
    n=int(input("Enter the height of the tree: "))
    n=n*2-1
    for i in range(1,n+1,2):
            print(" "*(n-i//2),"*"*i," "*(n-i//2))

chrismas_tree()
