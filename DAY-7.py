''' Usage of else with for -> the else keyword will only or execute when the
loop
is completely done without any break
'''
'''
# in this case when the entire loop execution is done we get result of
#else block
work_log = [0,1,1,1,0,1,0]
# result varable ->longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
            current_streak = current_streak + 1
            if current_streak > longest_streak:
                longest_streak = current_streak
                print(longest_streak)
                break
            #if break is removed the o/p will change
    else:
       current_streak = 0
else:
     print("Longest_Streak is : ",longest_streak)
print('Execute is Done')

#for-else with Notification scenario
# if Zero in list [0,0,0,0] then it is readed notification
# if One in list [0,0,1,0,1] the it is unreaded notification
notifications = list(map(int,input('Enter the values : ').split(',')))
for notification in notifications:
    if notification == 1:
        print('Have an unread notifications')
        break
else:
    print('no notifications')
'''
#While ->it relies on Condition,it will,be completely executed until the
# condition is satisified...
'''
Syntax while

while <condition>:
     Statement(S)...
     .......

i=0 # initialised statement
while i <= 10:
     print(i)
     i=i+1  # counter

# get the counter from 10 to 1
i=10
while i>=1:
    print(i)
    i=i-1
'''
# Banking scenario -> PIN authentication if more thean 3 attempts
# Account locked..

pin = input('My pin : ')
max_attempts =3
current_attempt = 1
while current_attempt <= max_attempts:
    entered_pin=input('enter the ATM PIN : ')
    if entered_pin == pin:
        print('login success')
        break
       #Continue #it holds for this condition and skip to the next part
    else:
        print('Try Again ')
        current_attempt +=1
else:
    print('Try again after 24 hours')
    
