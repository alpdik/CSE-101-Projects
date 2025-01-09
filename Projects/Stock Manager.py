stock=int(input("Amount of stock:"))
while stock>0:
    sales=int(input("Amount of sold today:"))
    stock2=stock
    stock -= sales
    if stock>0:
        print("You have",stock," cars left")
    elif sales>stock2:
        print("You can't sell more than you have")
        break
    else:
        print("Your stock is over")
        break
