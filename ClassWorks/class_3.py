"""
s=["sinjal","dahal",'a']
i=[10,20,30,50]
print(type(i))
print(type(s))
print(len(s)-1)
print(i[:2])
print(s[:2])

l=[]
print(l)
print(l.append(10))

a=[]
b=[20,30,40]
a.extend(b)
print(a)

a= [10,20,69]
print(a.pop(0))

a= [10,20,69]
a.remove(20)
print(a)

a= [10,20,69]
a[0]= 69
print(a)

a= (10,20,69)
print(type(a))        #doesnot support item assignment

a= (69,20,69)
print(a.count(69))

user1= ('Ram',564984)
user2= ('shyam',564984)
record = []
record.append(user1)
record.append(user2)
print(record)

#dictionary: key store value pair enclosed within {}

record = {"name":"ram","age":16,"address":"Thamel"}
print(type(record))

record["gender"]= "male"
print(record)
print(record["age"])
print(record.keys())
print(record.items())

r= {'name':('a','b'),'age':(10,20)}
print(r)
print(r['name'])
print(r['age'])
print(r['age'][-1])

# set is unordered collection of unique values
# python set is the implementation of mathematical set concept

s= {1,1,1,1,1,2,2,2,2,3,3,3,3,5}
print(s)            #Removes duplicate values

a= set("aaaaaaaaaaaaaaddddddddddddddbkjgsdddddddddueowwwwwwwwwvdbsoewfhdsvoefscba1554689561")
print(a)

s= {1,1,1,1,1,2,2,2,2,3,3,3,3,5}
a={69,69,1}
print(s^a)
print(s&a)
print(s-a)
"""
