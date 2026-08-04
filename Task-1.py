# even odd checker
num = int(input("enter a number:"))
if num == 0:
   print("zero is neither even nor odd")
elif num < 0 and num % 2 == 0:
   print("negative even number")
elif num < 0 and num & 2!=0: 
    print("negative odd number")
elif num > 0 and num % 2 == 0:
    print("even number")
else:
    print("odd number")
    print("---------\n")
# month
num = int(input("enter the month number:"))
if num in (12,1,2):
    print("winter")
elif num in (3,4,5):
    print("spring:")
elif num in (6,7,8):
    print("summer:")
elif num in (9,10,11):
    print("autumn:")
else:
    print("if month number < 12 inavlid:")
