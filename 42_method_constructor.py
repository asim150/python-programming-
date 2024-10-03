#constructor automatically get called in class creation
#mehtod need to get called
class DemoClass:
    a=10

    def __init__(self):
        print("welcome in constructor")


    def showval(self):
        print(self.a)


    def shop(self):
        print("welcome to junle")


obj=DemoClass()
obj.showval()
obj.shop()