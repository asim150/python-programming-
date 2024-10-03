l=[2,3,4,5,4,78,65]
l2=['heloo',40,60,67,70,5,6]

#zip  is use to  ietrate at same time two list also it print only in pair it ignore left element
for a,b in zip(l,l2):
    print(a,b)

#to ietratte all element of both list also the unpair extra element
a=len(l)
b=len(l2)
for h in range(a):
    print(l[h],l2[h])