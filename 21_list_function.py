l=[20,30,40,50]
print(l)

#delete function
del l[1]
print(l)

#pop function it delete to but it stored the pop element and can return it if user demand

print (l)
print(l.pop(1))

#remove  work on elemnt rather then  index
l.remove(20)
print(l)

#clear is use to clear the list
l.clear()
print(l)

#update is use to  update the element of list

l2=[32,5,67,4,63,4]
print(l2)
l2[3]=50
print(l2)

#insert function is use to insert any value at specific index

l2.insert(2,400)
print(l2)

#append use to insert at last also we can insert any list too and work on data type paste it as it was
l2.append(200)
print(l2)

# extend is  work  on inner value
n=[33]
l2.extend(n)
print(l2)

#count is use to count the frequency of element present
l3=[1,2,3,4,5,6,6,33,4,2,3,3,4]
a=l3.count(3)
print(a)


#max is use to find the hoghest value of list

a=max(l3)
print(a)
k=['wax','maxw']
m=max(k)
print(m)

#min is use to find minimum value of element

a=min(l3)
print(a)
k=['wax','maxw']
m=min(k)
print(m)

#sort is to sort in ascending and descending
l3.sort()
print(l3)

#reverse is use to reverse the data of list
l3.reverse()
print(l3)

#index is use to find index
p=l3.index(5)
print(p)