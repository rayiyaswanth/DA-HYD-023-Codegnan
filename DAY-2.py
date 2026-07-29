'''
Tokens --> variables, punctuators

Variables --> named memory location, it's a placholder for data
# Rules are to followed

'''
# MultiAssignment of variables

name,age,place = 'codegnan',7,'Hyd'
print(name,age,place)
print(name,age,place,sep=',')
print(name,place,age,sep='----->')

#Reassigning variables

#Swapping of two numbers :

name= "yashu"
a,b= 45,4.6
print(a,b)
a,b=b,a
print(a,b,sep=',')
c=b,a
print(c)

#Deleting the variables -->del

#del a
#print(a)
#del a,b
#print(a,b)  # after deleting if we print the same variables a,b ,
             #then it will show you error.

# Punctuators --> [](Lists),()(tuples),{}(Dict,sets)

name ="yashu " ; age=27 ; course="DA"
print(name,age,course)

#DataTypes -> Numeric (int,float,complex),boolean,None
           #->Sequences -->(lists,Tuples,Sets,Strings
           # Frozensets,Mappings(dict)

# Numeric type --> int,float,complex

# int datatype --> Defining the Integer . it's like normal numbers. 
age = 7
print(age)
print(type(age)) # It means returning the datatype of object
print(type(235)) # or finding the datatype of an object.

# float datatype -> defining the float and it's like a decimal numbers (2.5 ,6.1)
price = 750.40 ; discount =2.5
print(price,discount)

# Complex --> it's a combination of real and imag
# data =5 + 2i # it throws error .Because it is math cal .here "i" is imag repersentation

# Boolean --> True / False
valid =True
print(type(valid))
      
error= False
print(type(error))      

# TypeCasting --> Converting one datatype to another datatype
# Python by default follows implicit type(we need not mention the datatype)

# we will go for Explicit conversion

# Every built-in datatype is a built-in function
int, float,complex,bool

#Typecasting --> int --> float,complex,bool

age = 35
b = float(age)
print(type(b))
c = complex(age)
print(type(c))
d= bool(age) # returns True for existing data
print(type(d))
e= bool(0)
print(e)

# Float --> Other types

a=35.55
f=int(a)
print(type(f))
g=complex(a)
print(type(g))
h=bool(a)
print(type(h))

# example typecasting program

e = int(float(bool(45))) # bool show True and True means converting in to float it shows 1.0
                         # and converting to int now it show 1
print(e)

f = 45 + 2.5 + 2 +3j + False # here o/p is (49.5+3j)
print(f)




      
