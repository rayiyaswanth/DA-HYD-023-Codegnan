'''
Strings -> CaseConversion,Searching & Finding.String method,replace,Space removel.
'''
'''
# Searching,Finding,Replacing,joining....
a = "Codegnan"
print(len(a))
print(min(a))
print(max(a))

b=a.index('g') #it return index position
print(b)
c=a.index('n') #it return only the first occurance
print(c)
d=a.index('n',6) # it returns the next occerance
print(d)
#e=a.index('n',8) #value error
#print(e)
# f= a.index('t') #value error
#print(f)
g=a.index('n',1,6)
print(g)
'''
'''
#rindex() -> return last occurance
a="Codegnan"
b=a.rindex('g')
print(b)
c=a.rindex('n')
print(c) # here 'n' is occurance at 7th index
#d = a.rindex('n',8) # it returns value_error
#print(d)
'''
'''
#count() ->returns the number of items object is repeating
print("codegnan".count('n'))
#print('code'.count('w')) # it return 0 as we don't have 'w' in 'code'
print('cakshjasaksajia'.count('a'))

# find() -> first occurance but it avoid error return -1 if sucstring is not found
print('codegnan'.find('r')) # it returns -1
print('codegnan'.find('n'))

a="data"
print(len(a))
for i in a:
    print(a.count(i),a.index(i))

#replacing,Splitting,Joining
# Strings are Immutable
a='codegnan'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)
print(a.replace('x','yashu'))
print('gdsr#grohrsog'.replace('#',''))
'''
'''
a='code gnan python'
b=a.split() # by defalut if we have space it splits(returns list)
print(b)
print(len(b))
c='code,yashu,python'
d=c.split()
print(d)
e=c.split(',')
print(e)

# join()
a='code'
b='gnan'
# how it works
print(a.join(b))
print(b.join(a))
print('#'.join('yashu'))
print(' '.join('yashu'))
'''
'''
#String testing methods (boolean)
#isalpha(),isalnum,isdigit(),isupper(),islower.....

a='codegnan'
print(a.isalnum())# return s true for alphanumberic string else false
b='codegnan'
print(b.isalnum())
print(a.isalpha())#return true only for alphabets
print(a.isdigit())#return true only for digit string
print('810654932'.isdigit())
print('2345'.isnumeric())# this has upper edge (numbers,fractions,romans)
# startswith() ->how its starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))

print('Codegnan'.isupper('c')) # returns true for all uppercase
print('codegnan'.islower('c')) # returns true for all lowercase
print('Codegnan Python'.istitle())
'''
'''
# space removel -> strip() (removes leading and trailing space)

a=' codegnan '
print(a.strip())
b=input("enter the string : ").strip().lower()
print(b)
'''
print('123'.zfill(4))# zfill it means it will print or add zero before the output
# o/p : 123 -> 0123
print('123'.zfill(7))
#center(),ljust(),rjust() -> alignment of string (check length and then
#modify the width accordingly)
print('hai'.center(6))
print('hai'.center(6,'#'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))  
