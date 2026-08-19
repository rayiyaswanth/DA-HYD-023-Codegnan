"""
sequence --> dictionary -->collection of key value pairs which is used to store
JSOn format is in format of key value pairs
dict() -->mutable ,ordered and index through keys ,heterogenous, keys must be unique
and it can be int,float
data ={key:value}
"""

details ={}
#print(type(details))

details ={"ID":"22012A040624","Name":"yashu",
          "Gender":"m","Age":22,
          "place":"hyd","branch":"DA"}
#print(details)
#print(len(details))
"""#access the data from dictionary
#details[0] #keyError
print(details.keys())#it returns keys from the dictionary
print(details["ID"],details["Name"])
#if key name is not matching or it is invalid
#print(details["marks"])#it raises key Error as marks is not present
details["marks"] = []
print(details)
details["marks"].append(20)
print(details)
details["marks"].extend([24,15,23,10,20])
print(details)

#create a key value pair of practice session
details["PS"] = ("Tuesday","Thursday","Saturday")
print(details.keys())
#accessing the third day amrks of the student
print(details["marks"][2])
#accesing the 2nd day of practice session
print(details["PS"][1])
details["MI"] = ("Monday","Wednesday","Friday")
#operations --> mutable,Indexing through keys,Membership
print("Wednesday" in details)
print("MI" in details)#returns True as we have Mi as key
for i in details:
    print(i)#print keys one by one
for i in details.keys():
    #print(i)
     print(details[i])
     print(f"{i}:{details[i]}")
for i in details.values():
    print(i)
for i in details.items():#returns a key value pair
    print(i)
for key,value in details.items():
    print(f"key in {key}")
    print(f"value in {value}")

#update()-
details.update({"marks":[20],"PS":("Tuesday,Thursday","Saturday")})
print(details)
print(len(details))
details["marks"].extend([12,15,16])
print(details)
marks = list(map(int,input("enter the marks:").split(",")))
print(marks)
details["marks"].extend(marks)
print(marks)"""
print(details.keys())
print(details.get("keys"))
print(details.get("CS"))#it returns none as we dont have CS as key
print(details.keys())
#details.setdefault("Phone No","Portal")#if key is not present it inserts into dict
#print(details)
#details{"Phone No" = "9000959435","Portal" = "codegnan"}
#print(details)
print(details.pop("place"))#we need to mention key
print(details)
#details.pop()
#print(details)

del details["ID"]
print(details.keys())
details.clear()#removes all elements from dict
print(details)
#fromkeys
names =["yaswanth","yashu","rayi"]
b = (dict.fromkeys(names))
print(b)
b["yashu"] = 30
print(b)
c = dict.fromkeys(["ch443","ch624"]["Code","gnan"])
print(c)
#create a dictionary with your personal details which is similar to the the codegnan
#profile
