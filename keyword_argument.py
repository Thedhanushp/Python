def sample(name,age):
    print(name,age)
#this is keyword argument ,call any order
sample(age=20,name= "kevin")



def sample(num1,num2):
    sum = num1+num2
    return sum
result = sample(num1=20,num2=10)
print(result)


#Dictiory
values = {"name" : "kevin","place" : "uk"}
print(values)
#the values.get is used for only print the defind values
print(values.get("place"))