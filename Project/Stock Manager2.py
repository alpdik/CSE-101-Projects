stock=int(input("Amount of stock:"))
while stock>0:
    sales=int(input("Amount of sold today:"))
    if sales>stock:
        print("You can't sell more than you have")
        break
    stock -= sales
    if stock>0:
        print("You have",stock," cars left")
    else:
        print("Your stock is over")
        break

