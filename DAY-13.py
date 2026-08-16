'''
Sequences -> Strings,Lists,Tuples,Sets
Mapping ->Dictionary

#List -> Collection of heterogenous elements(items)
#LIst ->Index,ordered,Mutable,heterogenous,we use [] to store the data.

marks =[21,34,45,67]
print(marks)
print(len(marks))
print(type(marks))
#Operatior : Indexing,Slicing,Striding,Membership,merging,Repetition
'''
'''
#Nested Lists -> a list inside list

names =['yashwanth',22,8.3,[33,44,55],'DAY -1',56]

print(len(names))
print(names[3])
print(names[-3])

print(names[0][:4]) # if we put ':' before then it return code
print(names[0][4:]) # if we put ':' after then it return gnan
# get output as cdga from input.
print(names[0][::2])
names[0]=names[0][::-1]#return that what we are taking.
print(names[0])

print(names[3])
print(len(names[3]))
print(names[3][2])
#indexing ,Slicing -->Mutable
names[3]='good'
print(names)
# By indexing if we change the elements,length of collection will return same
names[3]=['boy','in','the','class']
print(names)
print(len(names))
print(names[3][1:3])

names[2:3]='yashu','is','good','boy'
print(names)
#In Slicing whatever elementd u pass as per logic length keep on increase
names[2:4]=['yaswanth','is a']
print(names)
'''
'''
#Create a nested list with string,list and work on indexing,slicing,striding
#added advantages if u could and strirng function also to it
#List Function -> append(),insert(),extend(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()

names=['codegnag','yashu']
# append() -> inserts single element to the end of the list
names.append('data')
print(names)
#names.append('analysis','agents') #type error
names.append(['analysis','agents'])
#append() will always increment the length of list by 1
names[3].append('chargbt')
print(names)

#extend() -> insert multiple elements to the end of the list

names.extend('analysis')#string will splitted and added to last
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,333,55,66])
print(names)
#names.extend(35,45)#type error
#print(names)
'''
# Insert() -> it will add or push before index in the list
names=['yashu','is','good','boy']
names.insert(2,'a')
print(names)
names.insert(-1,'AAA')
print(names)

# pop(),remove(),clear()

#pop() bt default last value or index erased,else given index
print(names.pop())
print(names)
#names.pop(Z)#gives error Z is not defined in input 
print(names)

#remove() we can remove a specific value
names.extend([23,14,15])
print(names)
names.remove(14)
print(14)

del names[1:3]# del keyword will apply permanent changes
print(names)

names.clear()#clear() will remove all elements and returns empty list
print(names)


