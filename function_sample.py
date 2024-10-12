def hey(*values):#the * used for passing unlimited arguments is called "arbitiory argument"
    print("first :"+values[0] + "\nsecond :"+values[1])

def hello():
    print("hello")
values = "kevin"
hello()
hey("hello","hey")



list = ["hello","hey",2]
#the append is used for adding same new values in the list
list.append("he")


# tuple is used for its also a list but not adding values after creating and not changing the position of the values
#tuple have no append
tuple = ("hello","hey","welcome",2) 