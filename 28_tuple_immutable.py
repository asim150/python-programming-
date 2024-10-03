#it is ordered,uses() and immutable
#also it  tuple cant have single variable
p=(5)
print(p,type(p))

t=(29,30,40,58,'hi','anla')
print(t,type(t))

#iterate using loop
l=len(t)

for i in range (l):
    print(t[i])

#also
for a in t:
    print(a)


k=(29,30,40,58,20)
#functions
#min
m=min(k)
print(m)

#max

m=max(k)
print(m)

#index
c=k.index(20)
print(c)


#count
c=k.count(20)
print(c)

#sum
c=sum(k)
print(c)

c=sum(k,100)# here we can add our numbere in tuples too
print(c)