'''
Sequences -> Strings,list,Tuples,Set,Frozenset
mapping -> Dictionary
'''
'''
#Sets -> A set is a unique collecction of objects,unordered,mutable,
#hashing,unindex,unique,Heterogenous
#set(),{}
#set will remove duplicates in set values.if any value repeate 2 times then it will print only one time.
#a = {} its an empty dictionary
a=set()
print(type(a))
stud_ids = {123,345,234,564,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))

#print(stud_ids[2]) -> typeError occurs

print(234 in stud_ids)
#print(stud_ids *2) #set can't be repeated
#print(stud_ids + stud_ids) #two sets cannot be merged.
'''
'''
data = {12,3,4,5,(1,2,3),'yashu'}
#data = {12,3,4,5,[1,2,3],'yashu'}
#data = {12,3,4,5,{1,2,3},'yashu'}
#print(data) #no lists inside a set (hashing technique) lista are Mutable
             #TypeError: unhashable type: 'list'

print(data)
print(len(data))
'''
'''
#Methods on sets -> add(),update(),remove(),discard(),pop()
#add() & Update() we use here.
names = {'sai','yashu','kiran','siva'}
print(len(names))
names.add('bablu')
#names.add('good','boy')#TypeError: set.add() takes exactly one argument (2 given)
print(names)
print(len(names))
names.add(('good','boy'))# here we passing Tuple then it willl execute o/p.
print(names)
print(len(names))

da_names={'mani','akash','sai','sonu'}

names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))
'''
'''
#remove(),discard(),pop(),clear()

da_names.remove('sai')
print(da_names)
#da_names.remove('sai') # keyError
#discard() ->  it will remove an element if it's present or not it will ignores.
           # -> it will not show any error in o/p.
da_names.discard('codegnan')
'''
'''
#pop() -> we don't what is removes and returns an ardritrary element
         # if we pop until set is empty then if we call pop again it shows error. 
da_names.pop()
print(da_names)
da_names.pop()
print(da_names.pop())# remove and return the element
da_names.clear()
print(da_names)
'''
'''
#copy() -> creates a shallow copy of set (independent of each other)
d=da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)
'''
#mathematical operations ->union(),intersection(),difference(),symmetric(),
#issubset(),issuperset(),isdisjoint()

da_23 ={12,23,34,45,23,36}
da_24={34,46,47,23}
'''
event = da_23.union(da_24)
#we can use that .union replace with this '|'
#event = da_23 | da_24
print(event)
print(len(event))
common =da_23.intersection(da_24)# .intersection() it shows only on common values in o/p
#intersection() also we can write like this '&'
#common =da_23 & da_24
print(common)
print(len(common))

common =da_23.intersection_update(da_24)
print(common)#it return 'None' in o/p
print(da_23) # common elements are finally stored.
'''
print(da_23)
print(da_24)
'''
diff =da_23.difference(da_24)
#diff =da_23 - da_24 #we can also write like this. using '-'
print(diff)
'''
'''
#.symmetric_difference() -> removes common elements and prints all
#elements from two sets
symm =da_23.symmetric_difference(da_24)
#symm =da_23 ^ da_24 #we can also write using like this ' ^ '
print(symm)

#issubset() -> checks for all elements to be present in other set
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint() returns false for sets having common elements
print(da_23.isdisjoint(da_24))
'''
#length od unique students ids in a class.where user can enter first input
#he should be given number of students_ids,he will enter students_ids

n=int(input())
student_ids=input().split()
result=set(student_ids)
print(result)
      


