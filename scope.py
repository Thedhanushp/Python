def check_scope():
    def do_local():
        test = "local test"
    def non_local():
        """ *declare the nonlocal they also takes the "test = default variable" 
            but the print conticion chnage and print the "non local test". """
        nonlocal test
        test = "non local test"
    def do_global():
        global test
        test = "global test"
        
    test = "default"
    do_local()
    # +test taking the "test=default" state not the function "do_local" test
    print("test value after do_local :"+test)
    non_local()
    print("test value after non_do_local :"+test)
    do_global()
    print("test value after do_global :"+test)#this global also print the same local test not the global state 

check_scope()
print("test value of main global :"+test)#in here this will print the main global variable outside the function
