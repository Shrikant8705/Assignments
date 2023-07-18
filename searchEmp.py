def searchEmp():
    id = int(input("Enter the id of the employee : "))
    fileRead = open("C:/Users/admin/OneDrive/Desktop/python/Assignments/empPackage/EmpDept.txt","r")
    print(fileRead.readlines()[id])
    