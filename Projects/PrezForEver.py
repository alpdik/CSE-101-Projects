Last_Elec= 2023
Curent_Prez= 12

def Elec_Calc (New_Prez):
    if New_Prez > Curent_Prez:
        print("The future president is going t0 be elected in", (New_Prez-12)*5+2023)
    else:
        print("The past president was  elected in", 2023-(12-New_Prez)*5)

year= int(input("Which presidents election date do you want to know?"))
Elec_Calc(year)
