# numeric Datatype --> int,float, complex along with boolean
# Input formatting --> Accepting input from the user  -> input()

# First Accepting integer input from user
'''
age = input('Enter the age : ') # by defalut input() accepts any input as String.
print(age)

# int (input()) -> will accept only integers
age = int(input('enter the age : '))
print(age)

# Float(input()) -> it accepts integer,float values
age = float(input('enter the age : '))
print(age)

# Accepting String input for user
name = input('Enter your name : ')
print(name)

# Accpet group of values
a = input('Enter Here : ').split() # in split() there is empty then it will add automatic space
                        # i/p -> yashu good boy o/p ->['yashu', 'good', 'boy']
print(a)

a = input('Enter Here : ' ).split(',')#if we want coma's in i/p then give like this.
                          # i/p -> yashu,good,boy o/p ->['yashu', 'good', 'boy']
print(a)

# List of integers
# map() must have at least two arguments.Like map(int,input) or map(str,input)
marks = list(map(str,input('enter the marks : ').split(',')))
print(marks)

#Now we want accept 2 values from user
age,salary = map(int,input('Enter the details : ').split(','))
print("age : ", age)
print('salary : ',salary)

#Here we have int,srt in one input
#o/p :
#Enter the details :yashu,23
#age :  yashu
#salary : 23
age,salary = input('Enter the details :').split(',')
print('age : ',age)
print('salary :',salary)

# Accepting input from user -> int,float -> input formatting

# Operators -> Operatord perform operators b/w values (operands)
# 7 types -> Arithmetic,Assigment,Comparision (Relationship)
# Membership,Identity,Logical,Bitwise

# Arithmetic Operators -. Arthmetic operations
# " + , - , * , / , // "
print(5+3)
print(5-3)
print(5*3)
print(5/3)# float value return here
print(5//3) # Floor division(integer division) ->returns qoutient

# Modulus ->divisible rules ->return remainder
print(5%3)

# Power (exponential)
print(5**3)

l,b = map(int,input("enter the values : ").split(','))
c=l*b
print('result : ',c)

# Assingment operators ->assign the values
# = ,+= ,-=
a=5
print(a)
#update the value of a
a=a+5 # a+=5 that = 5+5=10
print(a) #o/p -> 10

# Task : *= , /= ,//= ,%= ,**=

# Comparision Operators =. we compare the values -> boolean
# ==(equal to) , != (not equal to) , < (less that), > (greater than)
# <= (less than equal to) , >= (greater than equal to)

age = 35
print( age==35)
print(age!=25)      }
print(age < 35)     }all this are return boolean type true/false in o/p
print(age <= 35)    }
print(age >= 36)

print(-5 < -1)# returns boolean o/p : True

#Membership Operators -> in,not in -> shows in boolean type in o/p
#it checks for the existance of an object in a collection

marks = [56,75,45,85]
print(35 in marks)
#print(35 in 355) #TypeError

print(25 not in marks)
print('code' in 'codegnag') # checking code in codegnan word.
print('$' in 'abc$frg')# we can search symbols

#Logical Operators -> logical decision making -> and,or,not
# and ->all conditions to be satisfired
# or ->any one condition to be satisfied
# returns only in booolean type in o/p

a=(25 in [25,45,65]) and 44 < 53
print(a)
b= 45 > 56 or 25 <= 45
print(b)
c = not(True)
print(c)
'''
#Identity Operators -> check for identity of an object -> id()
# is, is not  -> returns boolean type
a=35
b=35
print(id(a))
print(id(b))
print(a is b)# o/p -> True
c=a
print(id(c))

a = [1,3,4,5]
print(id(a))
c=a
print(id(c))
print(c is a)
