# dictationary unordered data type
# work on key and value and key is unique
# d is the word used to define divationry


d={
    'name':'python',
    'fees':69000,
    'duration':'2months'
}

f=d['fees']
print(f)

for n in d:
    print(d[n])


#dicationary functions

#get
n=d.get('name')
print(n)

#keys
for a in d.keys():
    print(a)

#values

for a in d.values():
    print(a)
#items

for a,b in d.items():
    print(a,b)

#delete
del d['fees']
print(d)

#pop
d.pop('duration')
print(d)

#dit is use to create dictationry by passing key and value aat the same time
d=dict(name='putin', work='war')
print(d)

#update
d={
    'name':'python',
    'fees':69000,
    'duration':'2months'
}
d.update({'fees':50000000})
print(d)

#clear
d.clear()
print(d)

#insert
d['desc']="this is workoholic"
print(d)
