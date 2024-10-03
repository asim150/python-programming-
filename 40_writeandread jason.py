import json

file=open("post.json","r") #here we openning post.json in read mode
x=file.read()

finaldata=json.loads(x)  #cconverting dta to dict or list format

print(finaldata);

for a in finaldata:
    print(a['title'],a['userid'])


