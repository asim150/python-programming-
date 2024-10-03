
list=[1,2,3,'hello']
list2=[5,6,7,[3,4]]

print(list[0],list[3])

print(list[1:2])
print(list[0:])
print(list[1::2])

print(list[-1::-2])

print(len(list))
t=len(list2)
print(len(list2))
#iterarion using loop

for i in range(t):
    print(list2[i])

#iteration2nd method
for a in list:
    print(a)
#reverse a list


for b in range(t-1,-1,-1):
    print(list2[b])