

# ''' Program by me ''' ( Doesn't Satisfy Requirements )

'''
String = input("Enter a Sentance:")

print("Upper: ",String.upper())
print("Lower: ",String.lower())
print("Title: ",String.title())
print("Capitalize: ",String.capitalize())
print("Swapcase: ",String.swapcase())

'''

'''
user_input = input("Enter a sentence: ")
cases = ["upper", "lower", "title", "capitalize","swapcase","isupper"]
for case in cases:
    print(getattr(user_input, case)())
'''


# TASK --->

'''
Username = input("Enter a Username:")
while Username != "Quit":
    if Username.isalnum():
        print("Contains Only Letters and Numbers")
    else:
        print("Does not Contains Only Letters and Numbers")
    if Username.isidentifier():
        print("Begins with a Letter")
    else:
        print("Not a Valid Identifier")
    if Username.isascii():
        print("Contains Only ASCII Characters")
    else:
        print("Does not Contains Only ASCII Characters")
    if Username.isalpha():
        print("Contains only Letters")
    else:
        print("Does Not Contains only Letters")
    Username = input("Enter a Username:")
while Username == "Quit":
    print("Ended")
    break
'''       
        
        
        
