'''
Conditional statements in python:
it statements execute blocks of code when the conditio is true
Following are decicision statements

If statement
a=2
if(a<5):
    print(a)
    print(a+2)

    
Input in python

a= input()
if(a<5):
    print(a)
    print(a+2)

Type casting

a= input(int())
if(a<5):
    print(a)
    print(a+2)

# check +ve,-ve,zero number
a=int(input("Enter a number"))
if(a>0):
    print(f"{a} is positive")
elif: 
    print(f"{a} is zero")
else: 
    print(f"{a} is negative")

# Largest among 3
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if(a>b and a>c):
    print(f"{a} is largest")
elif(b>a and b>c): 
    print(f"{b} is largest")
elif(c>a and c>b): 
    print(f"{c} is largest")
else: 
    print(f"all are equal")

    
# nested statement
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if(a>b ):
    if(a>c):
        print(f"{a} is largest")
elif(b>a): 
        if(b>c):
            print(f"{b} is largest")
elif(c>a):
    if(c>b): 
            print(f"{c} is largest")
else: 
    print("all are equal")

listing of range
a= range(1,10)
print(list(a))

a= range(1,10,2)
print(list(a))


for loop

for i in range(5):
    print(i)

# print 1 to 10 except 2 and 4
for i in range(1,11):
    if(i==4 or i==2):
        continue
    print(i)

for i in range(4,11):
    if(i==6 ):
        break
    else:print(i)

for i in "Hello World":
    print(i)
'''

l = {'Name':"Ram",'age':55}
print(l)
for k,v in l.items():
    print(l[k])