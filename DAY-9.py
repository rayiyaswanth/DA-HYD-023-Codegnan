'''
#Task 1
n=list(map(int,input('Enter the values :').split(',')))
total=0
for i in  n:
     total +=i
print(total)
     
#Task 2
passkey=input("Enter the passkey :")
upper=0
lower=0
digit=0
special=0
for i in passkey:
    if 'A'<=i<='Z':
        upper +=1
    elif 'a' <=i<='z':
        lower +=1
    elif '0' <=i <='9':
        digit +=1
    else :
        special +=1
print('upper : ',upper)     
print('lower :',lower)
print('digit :',digit)
print('special :',special)
'
#Task 3
mails=input("enter : ").split(',')
for i in mails:
    print(i.split('@')[1])
'''
'''
o/p:enter : yashu@gmail.com,Yashu@amg.com
gmail.com
amg.com
'''
'''
movies =input("enter :").split()
i=1
for i in movies:
    print(i,movies)
    i+=1
'''    
#fiboncci series
'''
n=int(input('enter the value : '))
a,b=0,1
for i in range(n):
  print(a,end=" ")
  c=a+b
  a=b
  b=c
