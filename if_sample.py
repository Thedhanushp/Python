food = ["1.rice","2.fish","3.fry","4.sea food","5.biriyani"]
print(food)
choice = int(input("enter the food item : "))
if choice == 1:
    print("rice")
elif choice == 2:
    print("fish")
elif choice == 3:
    print("fry")
elif choice == 4:
    print("sea food")
else:
    print("biriyani")
print(choice,str("order is selected succesfully"))