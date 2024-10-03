import  random
#givign range to compure
r=random.randrange(1,101)

#user number
n=int(input("Enetr guess number "))
print("compuetr number is ",r)
print("your number is ",n)
if r>n:
    print("compuetr number is greater")
elif r<n:
    print("your number is less then compputer number")
elif r==n:

    print("you won")
else:
    print("invalid input")