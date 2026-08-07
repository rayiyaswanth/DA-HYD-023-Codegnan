'''
Identity Operatiors -> checks the identity of an object -->id().

a=5
b=a
print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)
print(5 == 5)

a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
# As we have Lists (Multable Collection),both c and a lista will have different
# id's where as values are same.
print(c is a)# o/p -> False , is-  means compare id of the variables or values 
print(c == a)# o/p -> True , == it means compare values
print(a is not c)# -> True

# Bitwise Operator ->  we perform bitwise operations over operands
# & (and) , | (or) , ^ (XOR) , shifting operators (<<,>>)

# Number will be converted to binary format
 print (5&3) # both 5 and 3 to be converted binary and bitwise and performed
 print (5|3) # bitwise OR
 print(5 ^ 3) # bitwise XOR
 print (5 and 3) # here and is logical operator for both existances
 print (5 or 3) # return 5 in above case

# leftshift operator << , rightshipt operator >>
print(5 < 1)# False comparision
print(5 << 1)# leftshift operation bt 1 position
print(5 >> 1)# right shift operation
print(15 << 2)# convert 15 to binary and perform 2 times shifting
print(15 >> 2)#  same 2 times right shifting

# input Formting  -> input(),int(input()) ,float(input())
# you know -> single input
# 2 or 3 inputs -> maps()
# group of integers -> list(map(int,input().split(',')))

name = input("enter the names : ").split(',')
print(name)

name1,name2 = map(str,input("Enter your names : ").split(',')
print(name1,name2)

# Tokens -> Numeric datatypes -> Operators -> flow of the program
# Control Block Statements -> they control the flow of the program
# when to execute, how to execute
# Conditional statements -> if,else,elif (rely on condition to be executed)
# Repetition Statement (Loops) -> for,while
                  
# Conditional statement -> if usage

Syntax :

if <condition>:
statements(s)...
....
age = int(input("Enter your age : "))
if age > 18:
    print('your age is : ',age)
    print('your are Allowed')

age = int(input("Enter your age : "))
if age >= 18:
    print("your age is :",age)
    print('your Allowed')
else:
    print("not Allowed")

# some case let's use only nested -> if ,else
age = int(input("Enter your age : "))
if age > 0:
    if age >= 18:
        print("Access Geanted")
    else:
        age=18-age
        print("you need to wait until",age,"years")
else:
    print("you have entered --ve values/Zero enter only +ve")
'''

