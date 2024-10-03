#list comprihension is use to compress the list or make it simple
#append is use to add elemnt in list
l=[]
for a in range (1,10):
    l.append(a)

# appended list
print(l)


#comprihensioning new list  also we can give condition too
# basically it filetr the list  by creating new list
n=[m for m in range(1,10) if m%2==0]

print (n)