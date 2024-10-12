def hey():
    print("hello")
hey()#calling the function
#next function definition
def hello(name):
    print("my name is "+name)
value = input("enter the name: ")
hello(value)

#multiple arguments

def hey(name,age):
    print("my name is : "+name + "\nage : "+str(age))
def hello():
    print("hello")
value = "Kevin"
hello()#2nd function calling
hey(value,19)#1st function calling
