'''
oop -> Class,Object,Method (__init__())
Encapsulation -> Public,portected,private
Inheritance -> It is one of the key feature of oop where we inherit
the properties (arreibutes/Methods) from one class to another class
(base class (parent class)) -> dervied class (child class)
Whatsapp -> personal user,Business user  (Catalog),Community connection 
Features -> Code reusability ,Avoiding code duplication,
code Maintainability, Polymorphism (Method Overriding (Super()) / Method Overloading, Operator Over loading __add__,___srt__)

Types : Single Inhetitance (Fingre print) 
--> One chlid class inheriting properties from one parent class
 Multiple Inheritance (Mother,Father -->Child)
--> One child class inheriting properties from two parent classes
Multilevel Inheritance (Grandparent ->Parent -> Child)
level by level
Hierarchical Inheritance -> Multiple child classes
inheritance properiting properties from single parent    
Hybrid Inheritance -> it can carry onr or more type of inheritances   
'''
'''
Syntax :

Single inheritance :

class baseclass:
    statements(s)..
    ....
class Derivedclass(baseclass):
    .......
    ........
'''
# Whatsapp Scenario -> personal User
'''
class user:
    """Single inheritance usage """
    def send_msg(self):
        print('sending msg')
    def voice_call(self):
        print('making voice call')
    def video_call(self):
        print('making video calls')
class businessuser(user):
    #pass
    def create_catalog(self):
        print("displaying products Catalog")

u1=businessuser()
print(dir(u1))
u1.send_msg()
u1.video_call()
u1.voice_call()      
u1.create_catalog()
'''
'''
#Social Media Login ->user -> update-users
class users:
    """single inheritance usage"""

    Company = 'Codegnan'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return self.fname + " " + self.lname


class update_users(users):

    def update_name(self):
        return self.fname.title() + " " + self.lname.title().strip()


u1 = update_users("yashu", "rayi")

print(u1.Company)
print(u1.full_name())
print(u1.update_name())

u2 = users("sai", "iit")

print(u2.full_name())
print(u2.Company)
'''
'''
class father:
    """usage of Constructor in  single inheritance"""
    def __init__(self):
        #self.property = 1000000
        self.property=100000
    def father_property(self):
        print(f'father property is {self.property}')
class kid(father):
    """now child class will have constroctor"""
    def __init__(self):
        self.property =200000
    def kid_property(self):
        print(f'kid property is {self.property}')    
    pass
obj = kid()
obj.father_propertys()            
obj.kid_property()
# in case it is giving same values for father and kid in o/p
#when we give property as same attribute in both class
# parent class and child class having constructor it means constructor overriding.
# here we use super()->key  to avoid the overriding
'''
# using super 
class father:
    """usage of Constructor in  single inheritance"""
    def __init__(self):
        #self.property = 1000000
        self.property=100000
    def father_property(self):
        print(f'father property is {self.property}')
class kid(father):
    """now child class will have constroctor"""
    def __init__(self):
        super().__init__()#calling superclass constructor
        self.cash=200000
    def kid_property(self):
        print(f'kid property is {self.cash}')    
        print(f'kid final property is {self.cash +self.property}')
    pass
obj = kid()
obj.father_property()            
obj.kid_property()