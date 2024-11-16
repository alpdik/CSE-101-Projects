def christmas_tree():
    height=int(input("Enter the height of the tree: "))
    base=height*2-1
    for i in range(1,base+1,2):
            print(" "*(base-i//2),"*"*i," "*(base-i//2))
christmas_tree()
