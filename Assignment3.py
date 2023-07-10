no1 = float(input("Enter First number:"))
no2 = float(input("Enter Second number:"))
choice = int(input("Please enter a choice:"))
if (choice == 1):
    print(no1 + no2) 
elif choice == 2:
    print(no1 - no2) 
elif choice == 3:
    print(no1 * no2) 
elif choice == 4:
    print(no1 / no2) 
elif choice == 5:
    print(no1 // no2)  
elif choice == 6:
    print(no1 % no2) 
elif choice == 7:
    print(no1 ** no2)
else:
    print("Incorrect Choice!")