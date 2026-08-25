'''
Constructor -> Instance method ->Public Attributes
Encapsulation :

Constructor -> it is a special method ( __init__()).
Which will automatically initialze the attributes and the methods
to the objects in the class.
'''
'''
class cars:
    def __init__(self,brand,name,price,color):
        self.brand=brand
        self.name=name
        self.price=price
        self.color=color
    def display(self):
        print("Car brand is : ",self.brand)
        print("car name is : ",self.name)
        print("Car price is : ",self.price)
        print("Car color is : ",self.color)
c1=cars(brand="tata",name="punch",price=10000,color="black")
c1.display()
print(c1.__dict__) # if we want to give another car details we use this  (__dict__) keyword
c2=cars(brand="toyota",name="supra",price=10000,color="white")
c2.display()
'''
'''
Encapsualtion -> it is one of the main feature of oop.
it binds (bundles) the data (attributes) and the methods (behavous)
into a single unit (class) -> multiple objects
-->Attributes -> Public,Protected,Private
#Public attribute --> Attributes define inside the class
and can be modified outside the class
'''
'''
class codegnan:
    """ codegnan portal with users"""
    def __init__(self):
        self.username=input("enter the student name : ")
    # To access the student details
    def display(self):
        print("Student user name is : ",self.username)
u1=codegnan()
u1.display()
print(u1.__dict__)# it return key-value pairs for attributes
u2=codegnan()
u2.display()     
'''

# Protacted attributes ->we use single underscore before an 
# attribute moreover it can be modified also outside the class
# and even accessible in subclasses...
'''
class codegnan:
    def __init__(self,username,_otp):
        self.username=username
        self._otp = _otp # we call this as protected attributed while we put ' _ ' before the attribute
    def display(self):
        print("user name is : ",self.username)
        print("student received otp :",self._otp)
u1=codegnan(username="yashu",_otp=6108)
u1.display()            
'''
#Private attributes -> we can special notation as doubleunder score '__'
#Accessible only inside the class and cannot directly
#modify
'''
class codegnan:
    def __init__(self,username,_otp,password):
        self.username=username
        self._otp = _otp # we call this as protected attributed while we put ' _ ' before the attribute
        self.__password=password #private attribute
    def display(self):
        print("user name is : ",self.username)
        print("student received otp :",self._otp)
        print("student passkey is : ",self.__password)
u1=codegnan(username="yashu",_otp=6108,password="yashu@123")
#u1.password() -> AttributeError is password is private
print(u1.__dict__)
print(u1._codegnan__password) #name mangling
'''
#using getter() and setter()
class codegnan:
    def __init__(self,username,_otp,password):
        self.username=username
        self._otp = _otp # we call this as protected attributed while we put ' _ ' before the attribute
        self.__password=password #private attribute
    def get_password(self):
        #return '******'
        return self.__password
    #to modify the password we use setter() method
    def set_password(self,new_password):
        if len(new_password) <= 6:
            print("wrong password")
        else:
            self.__password =new_password
            print("now password is updated")
u1=codegnan("yashu",6108,"yashu@123")
print(u1.get_password())
u1.set_password("yashu")
u1.set_password("yashu@1234")   
