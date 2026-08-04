'''
marks=int(input("enter the  marks(1-100):"))
if marks>=0 and marks<=100:
    if marks>=90: 
        print("user has secured grade A")
    if marks>=80 and marks<=89:
        print("user has secured grade B")
    if marks>=70 and marks<=79:
        print("user has secured grade C")
    if marks>=60 and marks<=69:
        print("user has secured grade D")
    if marks <60:
        print("user has failed,study again")  
else:
     print("enter only +ve values greater than 0 and less than 100")

#elif keyword --> if-elif-else
if <condition1>:
      statement(s).....
      ......
elif <condition2>:
      statement(s).....
elif <condition3>:
      statement(s).....
      .........
else
      statement(s).....
      
marks=int(input("enter the marks:"))
if marks <0 and marks>=100:
   print("entered values should be greater than 1 and less than 100")
elif marks >=90: 
     print("user has secured grade A")
elif marks>=80 and marks<=89:
     print("user has secured grade B")
elif marks>=70 and marks<=79:
     print("user has secured grade C")
elif marks>=60 and marks<=69:
     print("user has secured grade D")
elif marks <60:
    print("user has failed,study again")
else:
    print("no negative marks")  

# task ---> same usecase try with if-elif-else usuage in other way

#voter eligibility checkcase --> make sure to satisfy all possible conditions
#>=18 ---> access
#<18 --> no of years eligibility should tell
#negative values ---> not acceptable

age= int(input("enter the age:"))
if age>18 and age<=100:
    print("user has vote eligibiliy----")
    print("-----access granted-----")
elif age<18  and age >0:
    print("----user still need to get vote eligibility----")
    print("------- user need to wait for more",(18-age),", year(s)-----")
else:
    print("---- only positive values and less than 100 acceptable---")
'''
#output formatting ---> primt() --> we can pass any value  and also use sep and end
#output formatting ---> old style formatting (using commas)
#% usuage (%f,%d),.format() usuage,fstring notation
a,b=7,9
print(a)
print(b)
print(a,b)
name="codegnan";batch = "data analytics"
print(name,batch) #by default sep is having space
print(name,batch,sep='--------->')
#end= '/n', \t ---> tab space
print(name,batch,end='\t')
print(a,b)
name='codegnan';age=7;batch='DA-023';place='Hyderabad'
#Usage of comma
print(batch,'is in',name)#Variable and msg to be separated by comma
print(name,'is in',place,'age is',age,'years')
#old style formatting-->%d-->integer,%s-->string,f-->float
salary=24253.256
print("His salary is %d"(salary))
print("His salary is %f"(salary))
print("His Salary is %1f"%(salary))






