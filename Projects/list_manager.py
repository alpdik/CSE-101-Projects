def list_manager():
    list=[]
    i=int(input("How many integers do you want to add to the list: "))
    for x in range(int(i)):
        n=input(f"Enter the {x+1}. integer: ")
        list.append(int(n))

    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]

    print(list)

list_manager()