def a_tree():
    height=int(input("Enter the height of the tree: "))
    for i in range(1,height+1):
        print(f"{"a"*i}{"-"*(height-i)}")

a_tree()
