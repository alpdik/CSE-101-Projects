def taxcalc(salary,age):
    if 18<age and age<60:
        if salary<1000:
            tax=salary//10
        else:
            tax=salary//20
    else:
        if 18<age and age<60:
            if salary>=1000:
                tax=salary//4
        else:
            tax=salary//5
    return (f"${tax}")

x=int(input("Input the employees salary: $"))
y=int(input("Input the employees age: "))
print(taxcalc(x,y))