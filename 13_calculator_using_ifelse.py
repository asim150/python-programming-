x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
oper=input("enter the value of operation symbol..")

if oper=="+":
    print(x+y)
elif oper=="-":
    print(x-y)
elif oper=="*":
    print(x*y)
elif oper=="/":
    print(x/y)
else:
    print("invalide symbol")