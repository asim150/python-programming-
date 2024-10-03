l=[]
while True:
    c=int(input('''
    1 Push element
    2 pop element
    3 front element
    4 last eememnt
    5 display element
    6 exit '''))


    if c == 1:
        n = int(input("enter the value to push"))
        l.append(n)
        print(l)

    elif c == 2:
        if (len(l) == 0):
            print("Empty queue")
        else:
            del l[0]
            print("element is poped=", p)
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("empty queue")
        else:
            print("last queue value is ", l[0])
    elif c == 4:
        if len(l) == 0:
            print("empty queue")
        else:
            print("last queue value is ", l[-1])
    elif c == 5:
        print("display queue",l)
    elif c == 6:
        print("invalid  input")
        break;
