def ds(name, r_no): 

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
