'''
Procedure Oriented Programming
functions-->function is a block of code which performs a specific task,it is a reusable
block of code where we define using a def keyword
advantage -->  code reusablility,code maintainablity,eae of debugging,
avoiding code duplication..

def frames(paramters):  --> function def
    """Dog String"""  --> description
    statements....
    ....               ---> function body
    return value(s)...
frame(args)    -> function call


#perform sum of given objects
def add(a,b):
    "Sum of Objects"
    c = a + b
    return c
print(add(12,3))#addition
print(add("code","gnan"))#concatenation
print(add([12,14],[16,18]))#merging
c,d = map(int,input("enter the values:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    """Sum of objects withot return"""
    print(a + b)
add("code","gnan")
print(add(12,-34)) #it returns result along with none

name,age,salary = "yashu",20,000
#usage of return
def details():
    #return name,age,salary
    #return "codegnan"
    #return 12+10
    #return #--> #returns None as output
print(details())

There are 5 types of arguments

-->positional arguments
-->default argments
-->keyword arguments
-->variable length arguments(*args)
-->keyword variable length arguments (**args)

#Positional arguments -->Number of arguments in function defn should match
#with function call(order has to be maintained)
#len(12,34) this is as per built-in len(obj) will accept one argument

def details(name,place):
    """to store the details"""
    #name = "yashu"
    #place = "Hyd"
    #return name,place
    print(f'name is {name}')
    print('place is {place}') 
#print(details("yashu","thirupati"))
#print(details("sai","HYD"))
#print(details("yashu","tirupati",22)) # raises TypeError as only 2 arguments 

name,place = map(str,input("enter the values").split(','))
details(1,2)

#default arguments --> we can make arguments as default but not first argument as default

#def grocery(item="cheese",price=36):#we make all args as default
#def grocery(item="burger",price):#non default always follows default
def grocery(item,price=36): #as default we have given price as 36
    "usage of default arguments"
    print(f"The Item is {item} and price is {price}")
grocery("milk",32)
grocery(32,"milk")
grocery("bread")#as default we have given price as 36
grocery()#as both item and price as default arguments'''

#keyword arguments -->whenevr we wanted to specify the name of argument
def employee(name,salary,role,place="hyd"):
    """keywords argument usage"""
    print(f"employee name is {name},salary is {salary} and role is {role},work is {place}")
employee("yashu",20000,"admin")
employee(salary = 30000,role = "frontdesk",name = "yashu")
