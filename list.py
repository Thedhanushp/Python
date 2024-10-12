name = "hey hello"
names = ["crossroeds","testing","python"]
names[1] = "change"#this will be change the words from the 1 index,only in list
print(name[4])
print(names)
print(names[0])#only print the 0th index from the list
#Add new list adding with the 1 list 
names = names + ["py","zx","kevin"]
print(names)
"""
    .append is used for insert values into the end the list or any other
"""
#insert new value into the last position with the same list
names.append("hey kevin")
print(names)
#take from the user value to the end of the list
names.append(input("enter the value : "))
print(names)