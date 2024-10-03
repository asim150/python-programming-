import random
# randint is use to generate random number betweeb the rasnge passed and each time it print different number
n=random.randint(2,8)
print(n)

#randrange does same as randint but it does not include the range value it print till it but less then it
n=random.randrange(1,6)
print(n)

#random choice  gives any value of his choice fromt he list
l=[1,2,3,4,5,6]
j=random.choice(l)
print(j)

#random.random  print random values
r=random.random()
print(r)


#random.shuffle changes the position of elemtn/shuffle them anywhere
random.shuffle(l)
print(l)

#random.uniform print float value in the range
u=random.uniform(3,6)
print(u)