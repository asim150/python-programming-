class bikeShop:

    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bike ",self.stock)
    def rentBike(self,q):

        if q<=0:
            print("Enter the positive value or greatre then zero")
        elif q>self.stock:
            print("Enter the value (lee then stock)")

        else:
            print("Total Price",q*100)
            print("Total  Available Bikes",self.stock-q)


while True:
    obj=bikeShop(100)
    uc=int(input('''
    1 Display stocks
    2 Rent  a Bike
    3 Exit '''))

    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter the Qty:---"))
        obj.rentBike(n)
    else:
        break