#polymorphism has overloading and overriding
#polymorphism means same function name but different signature being uses for different type


#same function but different parameter
class A:
    def display(self,name=''):
        print("welcome to jungle A  hehe "+name)


obj=A()
obj.display()
obj.display(' A')


#overriding is function with same name in different class and are onherited thus  function over ride the first function 
#here function of b over ride the function of a

class B(A):
    def display(self,name=''):
        print("welcome to jungle B hehe "+name)

obj=B()

obj.display(' B')

# to avoid overriding we use   super function

class B(A):
    def display(self,name=''):
        super().display()
        print("welcome to jungle B hehe "+name)

obj=B()

obj.display(' B')