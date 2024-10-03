#simple function
#def is define keyword for function create

#creating function
def asmfuncrtion():
    print("welcome to the hub")
#calling function
asmfuncrtion()

#arguement function
def sumdata(a,b):
    print(a+b)
x=int(input("enter x value"))
y=int(input("enetr y value"))
sumdata(x,y)


#defaukt function
def minus_data(a,b=8):
     print(a-b)
minus_data(20)

# return keyword use
def multi(a,b=6):
    c=a*b
    return c
k=multi(4)
print(k)
