import random
l=['Rock','Paper','Scissor']

r=random.randrange(1,4)

while True:
    ucount=0
    ccount=0
    n = int(input('''
    Game start.......
    1 Yes
    2 No||Exit
    '''))
    if n==1:
        for a in range (1,6):
            userinput=int(input('''
            1 Rock
            2 Paper
            3 Scissor
            '''))

            if userinput==1:
                urchoice="Rock"
            elif userinput==2:
                urchoice="Paper"
            elif userinput==3:
                urchoice="Scissor"
            compchoice=random.choice(l)

            if compchoice == userinput:
                print("Draw")
                print("your choice is :", userinput)
                print("Compuetr coice is:", compchoice)
                ucount=ucount+1
                ccount=ccount+1
            elif ((urchoice=='Rock' and compchoice=='Scissor')
                  or (urchoice=='Paper' and compchoice=='Rock')
                  or(urchoice=='Scissor' and compchoice=='Paper')):
                print("your choice is :", userinput)
                print("Compuetr coice is:", compchoice)
                print(" you won")
                ucount = ucount + 1

            else:
                print("your choice is :",userinput)
                print("Compuetr coice is:",compchoice)
                ucount = ucount + 1
                print("Compuetr won ")   
        if ucount==ccount:
            print("Final game draw")
            print("your score is:",ucount)
            print("compuetr score is:",ccount)
        elif ucount>ccount:
            print("Final game you won")
            print("your score is:", ucount)
            print("compuetr score is:", ccount)
        else:
            print("Final game compuetr won")
            print("your score is:", ucount)
            print("compuetr score is:", ccount)

    else:
        break

