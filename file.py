#provide the path and provide the permission with the help of google ith automatically create the file
f = open("file2.py","w")
#for read
with open("file2.py","r") as f:
    x = f.read()
print(x)


f.write("print('hey')")
f.close()