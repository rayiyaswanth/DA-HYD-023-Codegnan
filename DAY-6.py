'''
conditional Statements -> control of flow of execution of the program
                       -> conditional Statements -> if,elif,else..
                       -> Repetition Statements(Loops) -> for,While (for with else)(While with else).

                       -> Jumping Statements -> break,continue,pass.

'''
#Loops -> this are helpful for repetition (Automative tasks)
# for keyword will be helpful to iterate over a sequence / range
#Syntax for (for keyword):
'''
for <variable> in sequnce/range :
    Statement(s)..
    ....
'''

#range(start,stop,step)
#by default range picks 'Zero' as start value.
'''
for i in range(5): 
    print(i)

#in above case we got 10 iterations
#In range(stop) -> default 0 ends at end-1
for i in range(1,10):
    if i > 5 and i%2==0:
        print(f'The final value of i is --> {i}')
'''
# range (start,stop,step) --> here step --> interval
'''
for i in range(1,10,2):
        print(i)
#print -10 to -1
for i in range(-10,0,1):
    print(i)
#print 10 to 1
for i in range(10,0,-1):
    print(i)

#[] -> we generally lists
names = ['yashu' ,'sai','ram']
print(len(names))#len(obj) -> returns the number of itemss in a container
print(names)
for name in names:
    if name == "ram":
       print("student name is : ",name)

#Calculate the sum of firt 10 numbers
result =0
for i in range(11):
  if i%2==0:
      result= result + i
print(result)      
'''
# understand the loops usage fitness streak example
# work_out ->1,work_out_missed ->0

work_log = [0,1,1,1,0,1,0]
# result varable ->longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
            current_streak = current_streak+1
            if current_streak > longest_streak:
                longest_streak = current_streak
    else:
       current_streak = 0
print(longest_streak)
