import datetime
x=datetime.datetime.now()
print(x)

# specifying the date time format
print(datetime.datetime(2024,4,5))


#%y gives the year
m=x.strftime("%y")
print(m)
m=x.strftime("%Y")
print(m)

#%b month name
m=x.strftime("%b")
print(m)

#%m month as number
m=x.strftime("%m")
print(m)

#%H hour
m=x.strftime("%H")
print(m)

#%I hour
m=x.strftime("%I")
print(m)

#%p am/pm
m=x.strftime("%p")
print(m)

#M minute
m=x.strftime("%M")
print(m)

