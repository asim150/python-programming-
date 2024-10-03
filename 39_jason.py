#json is java script object notation
#use to storen and transfer data bnetween the browser and server and make communicartion between them by api
#json is text,written with javascript objet notation
#python too support JSON with built in packages called jason
#also used in javascript ,java ,backend

#json support string,num,bool,null,object,array data types

#converting dictationry to json and it gives output in dictationry format
import json


d={
     'course_name':'python',
     'fees':150000
}

f=json.dumps(d)
print(f,type(f))

#loads convert to dictationry
k='{"course_name":"python","fees":150000}'
f=json.loads(k)
print(f,type(f))