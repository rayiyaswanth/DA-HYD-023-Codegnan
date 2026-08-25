'''
OOP --> Object Oriented Programming
An Object Oriented Programming is a mechanism or a process which revolves around creating objects,it consists of two
different properties
-->Attributes and -->methods
A Method is a function defined inside a class which carry the behaviour of the object.
An object is an instance (physical thing) which utilises the class.
ex
Chair (object)-->Wood,Tools,Dimensions(blue print),Carpenter.
The Main Features of OOP-->Modularity,Scalability,Encapsulation(binding the data (attributes),features to the class) (object)
Abstraction -->Show only relevant information to the class (object)
Inheritance -->Acquring properties (attributes,methods)
singe -->Fingerprint
Multiple -->Parents (Mother,Father) -->Child
Multilevel --> grandParent -->parent -->child
Polymorphism -->Method Overloading,Method Overriding,Operator Overriding.
'''

#syntax for class creation :
'''
class class_Name:
    """Doc String"""
    attributes (charecteristics)
    ..........
    def func(self): (it gives the behaviour of the class)
        .....
        ......
    .....  
obj = class_Name()

#Student Class with bacis details
class Student:
    """Understanding the usage of OOP"""
    name = "bhavitesh"
    id = "CGH3555"
    gender = "male"
    email_id = "bhavitesh.b2001@gmail.com"
    #Methods (behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'student ID is {self.id}')
        print(f'student Mail id is {self.email_id}') 
u1 = Student()
print(u1) 
#print(dir(u1)) #dir stands for directory (returns all available methods/attributes)           
u1.display()
u2.display()

#Student Class with Multiple objects
class Student:
    """Understanding the usage of OOP"""
    name = input("Enter the name:")
    id = input("Enter the ID No:")
    gender = input("Enter the Gender:")
    email_id =input("Enter the Mail id:")
    #Methods (behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'student ID is {self.id}')
        print(f'student Mail id is {self.email_id}') 
u1 = Student()
u1.display()
u2 = Student()
u2.display()
print(u1.__dict__()) #it returns empty disctionary
print(u2.__dict__()) #it returns empty disctionary
'''
'''
#students details with multiple objects
class Students:
    """Understanding the usage of OOP"""
    def data (self,name,id,gender,email_id):
        self.name = name
        self.id = id
        self.gender = gender
        self.email_id = email_id
    #Methods (behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'student ID is {self.id}')
        print(f'student Mail id is {self.email_id}') 
        u1 = Students()
        u1.data("bhavitesh","3555","male","bhavitesh.b2001@gmail.com")
        u1.display() 
        print(u1.__dict__)
        u2 = Students()
        u2.data("Akash","3555","Male","bhavitesh.b2001@gmail.com")
        u2.display()
        print(u2.__dict__)
'''
#Create car details :

class cars:
    def data(self,brand,name,price,color):
        self.brand=brand
        self.name=name
        self.price=price
        self.color=color
    def display(self):
        print("Car brand is : ",self.brand)
        print("car name is : ",self.name)
        print("Car price is : ",self.price)
        print("Car color is : ",self.color)
c1=cars()
c1.data(brand='BMW',name='BMW_mk24',price=20000,color='black')
c1.display()

