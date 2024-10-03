#inherite the chraracter of a clss into other class

class A:
    def displayA(self):
        print("father")

class B(A):
    def displayB(self):
        print("child here")

class C(B):
    def displayC(self):
        print("children here")

obj=B() # ccreating object of B only and cliing both class as A is inherited
obj.displayA()
obj.displayB()

obj1=C() # ccreating object of c only and calling both class as A and B too is inherited
obj1.displayA()
obj1.displayB()
obj1.displayC()