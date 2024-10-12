#class
class Mysampleclass:#class have no brackets only full colun
    def hello(self,n):#declare any local name here
        self.name = n
    def print_name(self):
        print(self.name)
    
    
#for calling the class create a "object"
x=Mysampleclass()
y=Mysampleclass()
name = "kevin"
#the self means that x will call the self and working the function 
x.hello(name)
y.hello("hey hello")

x.print_name()
y.print_name()