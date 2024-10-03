#method overloading is concept of polymorphis ,elelmtn of oops,
#method has same name but different arguement,or how many arguement

class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print(a*b)
        elif a!=None:
            print(a*a)
        else:
            print("nothing")

#arguement difference causes overloading
obj=Area()
obj.find_area()
obj.find_area(2)
obj.find_area(10,20)

#overriding having same name same arguement,also implement with inheritence ,mostly used to reduce the meomory
class A:
    def display(self):
        print("welcome to jungle A  hehe ")

class B(A):
    def display(self,name=''):
        print("welcome to jungle B hehe ")

obj=B()
obj.display(' B')
