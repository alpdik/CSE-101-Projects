def list_manager():
    list=[]
    i=int(input("How many integers do you want to add to the list: "))
    for x in range(int(i)):
        n=input(f"Enter the {x+1}. integer: ")
        list.append(int(n))

    for x in range(len(list)):
        if x==0:
            continue
        if list[x]<list[x-1]:
            temp=list[x-1]
            list[x-1]=list[x]
            list[x]=temp

    print(list)

list_manager()