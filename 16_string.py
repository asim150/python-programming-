w=("helloaaism ismheree")
#indexing
print(w[0])
print(w[12])

#slicing
print(w[0:7])

print(w[0::2])# 2 is skipping evry 2 numer and blank space mean till last data

print(w[-1::-1])#from last to first# revesre too

#iteration of string
t=len(w)
print("length of w string is",t)

for n in range(t):
    print(w[n])

#reverse 2nd method the string
for n in range(t-1,-1,-1):
    print(w[n])

