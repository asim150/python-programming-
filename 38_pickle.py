#pickle is library used to serialize and deserialize  data which mean to store and read data
#pickles data types are:-bool,int,float,complex numbr,string,tuples,list,set and dictattiomary

#pickle has two fumction: dump set ther data serialize  AND Load deserisalise the data
#import module is use to import pickle
#pickle use two mode rb-data load,wb-data write

#use to dumb
import pickle
l=[1,2,3,4,5]
file=open("writedata.txt","wb")
pickle.dump(l,file)
file.close()



#use to file
file=open("writedata.txt","rb")
l=pickle.load(file)
print(l)