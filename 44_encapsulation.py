# an object variaable should not always be directly acesseble
#method are use to set variabvle are set correctly
class student:
    def __init__(self):
        self.__name=""# private variable

#getter function
    def getname(self):
        return self.__name


#setter function
    def setname(self,name):
        self.__name=name

obj=student()
obj.setname("Testing")
x=obj.getname()
print(x)

# encapsulated here name is created secretly as private ands cant be acces directly

class student:
    __name="asim"
    def __init__(self): #constructor created
        print(self.__name)

        self.__display() # accessing  function from inside
    def __display(self):
        print("here you are ")

obje=student()
