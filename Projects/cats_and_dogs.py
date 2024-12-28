class Dog:
    def __init__(self,total_donation=0):
        self.total_donation = total_donation

    def add_donation(self, donation):
        self.total_donation += 2 * donation
        return self.total_donation

class Cat:
    def __init__(self, total_donation=0):
        self.total_donation = total_donation

    def add_donation(self, donation):
        self.total_donation += donation
        return self.total_donation

def main():
    dog = Dog()
    cat=Cat()
    while True:
        pet_type = input("pet type? ")
        if pet_type == "d":
            donation = int(input("donation? "))
            dog.add_donation(donation)
            print("Current amount for dogs is", dog.total_donation)
        elif pet_type == "c":
            donation = int(input("donation? "))
            cat.add_donation(donation)
            print("Current amount for cats is", cat.total_donation)
        elif pet_type == "q":
            print("amount for cats is", cat.total_donation, "amount for dogs is", dog.total_donation, "total amount is", cat.total_donation + dog.total_donation)
            break

main()