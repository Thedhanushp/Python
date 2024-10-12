class student:
    def hello(self,n):
        self.name = n
    def print_name(self):
        print(self.name)
     
          
x = student()
y = student()

name = "kevin"
x.hello(name)
y.hello("hey hello")

x.print_name()
y.print_name()
        