print("mutble-list,dictationry,byte array","where value can be changed")

print("immutable-int,float,complex,string,tuple,set","where value cannt be changed")

a=2
b=3.4
c=2+4j
print(a,type(a))
print(b,type(b))
print(c,type(c))

s=("the ran he she @ ur")
print(s,type(s))
#list uses square  bracket
l=[12,'rr',34]
print(l,type(l))

l[2]=44
print(l)

#tuple it is faster then list and uses round  bracket as no updation,insertion not allowed as it is immutable
t=(132,"strfefe",33)
print(t,type(t))

#dictationary
d={
    'name':'asim',
    'age':'23'

}
print(d,type(d))
print(d['name'])

#set unique elemt uses curly braces too

s={20,47,23,'f'}
print(s,type(s))





