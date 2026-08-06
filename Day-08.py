'''
Tokens-->Keywords,Identifiers,Literals,Operators,Punctuators,variables
Operators --> Numeric data(int,float,complex),bool
control flow -->if,elif,else,for,while
Sequences --> strings,lists,sets,tuples,mapping(dict)
'''
#string --> Group of characters , we use single or doubleor triple quotes
#for representation of strings...
#strings are Immutable,ordered,indexed collection
#space is also character
'''
name = 'codegnan'
print(name)
print(type(name))
print(len(name))#len-->returns the no of items in container
'''

#index() --> fetch the object (position) starts at o and ends at len(obj) - 1
#we use [] representation
'''
name = 'codegnan'
print(name[5])
#print(nname[25])#raises INDEX ERROR --> as its out range

#negative indexing --> -1 to len(obj)
print(name[-1])
print(name[-6])
'''

#Slicing --> we can access group of characters(object)
#we use [start:end] #start default --> 0,start is included,end is excluded
'''
name = 'codegnan'
print(name)
print(name[:])#returns entire string
print(name[0:])#returns entire string
print(name[:4])#starts at 0th index before 4th index
print(name[1:5])
'''
'''
name='python'
print(name[3:7])
print(name[7:3])#returns an empty strings are immutable
#slicing is applicable from lower index to higher index
print(name[:45])#returns till end of the string
print(name[:45])#returns empty

print(name[-1:-5])#returns empty
print(name[-5:-1])#start at -5 and ends at -2
print(name[-2:])
print(name[-5:4])

print(name[1:3:6])
'''
#stridding--> [start:end:step]
'''
course = 'DataAnalysis'

print(len(course))
print(course[:4])
print(course[4:])
print(course[-3:])

print(course[::1])#returns all characters
print(course[::2])#includes start to end skipping1 character

print(course[1:6:3])
print(course[2::3])
'''
#Task:workout with all possibilities of slicing and stridding on an example
'''

name='codegnan'
#name[3] = 'w' #strings are immutable

#operations on strings --> Indexing , concatenation , repetition
print(name*3)
print('*'*25)

#concatenation -> combining strings

data='saketh'+'python'+'DA'
print(data)
print('123'*4)#numeric string
print('code' in 'codegnan')

for i in 'codegnan':
    print(i)
#in above case we get every character line by line
'''
'''
for i in 'codegnana':
    print(i,end=' ')
'''
'''
name = "datacodegnan"
#Built-in function --> len(),min(),max(),sorted()
print(len(name))
print(min(name))#alphabetical order ASCII ordering
print(ord('A'))
print(max(name))
print(chr(97))
print(sorted(name))
'''

#methods on strings --> case-conversion,finding/searching...
'''
name = 'Codegnan data'
#case- conversion --> upper (),lower(),title(),capitalize()
a=name.upper()
print(a)
b=name.lower()
print(b)
'''
name='CodegnAn nOt'
#captalize()-> converts firts letter to upper case
'''
c=name.capitalize()
print(c)
d=name.title()
print(d)
'''


#Task:A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strngs to return A-Z

for i in range(65,91):
    print(chr(i) , end =" ")

























































































