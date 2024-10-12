"""multi line comment
    more line comment
"""

a = int(input("enter the value: "))
b = int(input("enter the 2nd: "))
print(type(a))
print(type(b))
temp = a
a = b
b = temp
print("swaping is A is : "+str(a) + " B is: "+str(b))