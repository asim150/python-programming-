# set is unordered ,unindex,unique data,{}

s={29,1,3,4,4,343,543}
print(s) # here it eleminate duplicate automatically

#iterate
for a in s:
    print(a)

# functions:=

# set() this function convert list ,tuples to set()
l=[2,4,6,21,3]
i=set(l)
print(i)

#add is use to add element at end

i.add(200)
print(i)

#pop use to delete element randomly
s.pop()
print(s)

#remove is use to delete element by passing value
s.remove(29)

#discard is also usw to delete elemnt by passing value
s.discard(3)

#clear use to delete all element of set
s.clear()
s={29,1,3,4,4,343,543}

#update is use also it does not update alreadt present element
p={4,5,7,3,23,0}
s.update(p)