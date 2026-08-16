
'''
#secrey number guessing:
secret_number = 123
guess = None
print("Welcome to the Number Guessing Game!")
while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the secret number (123)!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# otp verification:
otp = "1777"
max_attempts = 8
current_attempt = 0
while current_attempt <= max_attempts:
    entered_otp = input("Enter the otp:")
    if entered_otp == otp:
        print("Login_successful")
        break
        #continue #it holds for this conditions and skips to the next part 0
    else:
       print("Entered otp is wrong..Try again carefully")
       current_attempt +=1
else:
    print("Account Locked,try after 24hours.")

#restaurent:
food = input("pizza,burger,kfc")
count = 0
while food != "exit":
    count += 1
    food = input("pizza,burger,kfc")
print("total number of items ordered",count)
'''
# secret identifier:
secret="game"
current_attempt = 0
max_attempts = 3
while current_attempt <= max_attempts:
    a = input()
    if (a == secret):
       print("access granted")
       break
    else:
        remaining = max_attempts - current_attempt
        print(f"wrong guess and you have only 2 attempts:")
        current+=1
else:
     print("chances over")
    
