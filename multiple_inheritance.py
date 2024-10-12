class First:
    def display_firts(self):
        print("first")
           
class second():
    def display_second(self):
        print("second")
        
   
#inharit        
class third(First,second):
    def display_third(self):
        print("third")
        
        
x = third()
x.display_third()
x.display_second()
    
#identifing the order of the class inheritance
print(third.mro())