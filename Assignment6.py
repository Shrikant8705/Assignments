# 1)Create a function named ds with parameters roll_no and name.
# 2)Add those parameters in the following data structures:
# list, tuple, sets and dictionaries
# 3) After adding values
# change the values during runtime
# 4)Delete these data structures

def ds(name, r_no):
    
    # Assigning the initial values 

    lst = [name,r_no]
    tup = (name,r_no)
    sets = {name,r_no}
    dic = {
        "Name":name,
        "Roll_no":r_no
        }
    
    print(lst)
    print(tup)
    print(sets)
    print(dic)
    
    
    newName = str(input("Enter a Name : "))
    newR_no = int(input("Enter a Roll number : "))
    
     
    lst[0] = newName
    lst[1] = newR_no
    tup = tuple(lst)
    set.update(set(lst))
    dic["Name"] = newName
    dic["Roll_no"] = newR_no
    
    print("Updated data structures are: ")
    print(lst)
    print(tup)
    print(sets)
    print(dic)
    
    
    print("Deleting the data structures!")
    del lst,tup,sets,dic
    print("Data Structures are deleted.")
    print("Bye!")
 

ds("Shrikant",117)