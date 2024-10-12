def check():
    def rice():
        nonlocal key#using for nonlocal will take the inside key value in the rice
        key = "actual key"
    def sugar():
        key = "default key"
    def local():
        global key
        key = "main local"
    def non_local():
        key = "non local"
    
    key = "Hello user"
    rice()
    print("the rice is :"+key)#the key will print the local key state not the rice nonlocal key
    local()
    print("the global is :"+key)
check()    
print("the main global is :"+key)