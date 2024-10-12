class BaseClass:
    #contractor
    def __init__(self):
        print("base init")
        
    def set_name(self,name):
        self.name = name
        
 #inherit
 #the subclass have a brackets and inside the bracket mention the baseclass name       
class SubClass(BaseClass):
    def __init___(self):
        super().__init__()
        print("sun class")
        
    def set_name(self,name):
        super().set_name(name)
        print("sub class setname")
           
    def welcome(self):
        print("welcome")
    
    def display_name(self):
        print("Name : "+self.name)
        

y = SubClass()
y.welcome()
y.set_name("kevin")
y.display_name()