class sample:
    def set_name(self,name):
        self.name = name
    
    #special add fun
    def __add__(self,second):
        name = self.name+" "+second.name 
        return name  
    
first_name = sample()
second_name = sample()

first_name.set_name("kevin")
second_name.set_name("don")

#add the name to full name
full_name = first_name + second_name
print(full_name)
