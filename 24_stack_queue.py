#stack first in last out //FILO

l=[]
while True:
    c=int(input('''
    1 Push element
    2 pop element
    3 peek element
    4 display element
    5 exit '''))

    if c == 1:
        n = int(input("enter the value to push"))
        l.append(n)
        print(l)

    elif c == 2:
        if (len(l) == 0):
            print("Empty stack")
        else:
            p = l.pop()
            print("element is poped=", p)
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("empty stack")
        else:
            print("last dtack value is ", l[-1])
    elif c == 4:
        print("dis[lay stack", l)
    elif c == 5:
        print("invalid input")
        break;




#queue first in first out //fifo