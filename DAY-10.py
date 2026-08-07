'''
# cricket total score ...
b=[4,6,1,0,2,4,0,6]
score =0
boun =0
db=0
for i in b:
    score +=i
    if i==4 or i==6:
        boun +=1
    elif i==0:
        db +=1
print(db)
print(boun)
print(score)
'''
'''
#about ATM pin attempts..
pin = "1777"
max_attempts = 3
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("Enter the ATM PIN:")
    if entered_pin == pin:
        print("Login_successful")
        break
    else:
       print("Entered PIN is wrong..Try again carefully")
       current_attempt +=1
else:
    print("Account Locked,try after 24hours...")
'''
# pattern attempt..
passkey ="Yashu@6108"
max_attempts=5
current_attempt=0
while current_attempt <= max_attempts:
      enter_passkey=input("enter the passkey : ")
      if enter_passkey == passkey:
          print("passkey correct login success ")
          break
      else:
          print("incorrect passkey pls try again !")
          current_attempt +=1

