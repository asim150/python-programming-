#functions
print("lower,upper,title,capital")
print("find,index,isalpha,isdigit,isalnum,chr,ord")
s="Welcometojungle"

print(s.lower())
print(s.upper())
#title print first letter of every word as capital
print(s.title())

#capiatl make fisrst letter capital
k="soua"
print(k.capitalize())


# find function use to find element in senetence or number etc
print(s.find('e')) #return index number of the element
print(s.find('e',2))# start the search from 2nd index

#index function return index
print(s.index('j'))

#isalpha to see all stirn char are alphanbet
print(s.isalpha())

#isdidgit  is to cehckk presentce of digit
print(s.isdigit())

#isalnum check for num or alphabet in any  sring word or combination
print(s.isalnum())

#chr take integer  value and return character in form of string

y=34
a=66
print(chr(y))
print(chr(a))

#ord takes string value and return integer

y="a"
x="A"
print(ord(y))
print(ord(x))