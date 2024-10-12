class SampleClass:
    year = 2024
    #constructor(used for automatically called all objects)
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
        
    def add_age(self):
        self.age = self.age + 1
        
    def relocate(self,place):
        self.place = place
        
    def display_all(self):
        print("year : "+str(SampleClass.year))
        print("name : "+self.name)
        print("age : "+str(self.age))
        print("place : "+self.place)
        
    # used for commenly keeping data and commenly share   
    @classmethod
    def add_year(cls):#declare any name here
        SampleClass.year = cls.year + 1
        
    #without any effections in the code for printing commenly anything or any where  
    @staticmethod
    def dispaky_welcome():
        print("welcome")
    
    
SampleClass.dispaky_welcome()   
      
x = SampleClass("kevin",20,"uk")
y = SampleClass("don",19,"russia")

SampleClass.year = SampleClass.year + 1
 

x.add_age()
y.add_age()

x.display_all()
y.display_all()

print("----------------")

SampleClass.add_year()

x.relocate("delhi")
y.relocate("mumbai")

x.display_all()
y.display_all()
