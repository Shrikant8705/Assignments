def showEmp():
    fileRead = open("C:/Users/admin/OneDrive/Desktop/python/Assignments/empPackage/EmpDept.txt","r")
    for i in fileRead.readlines():
        print(i)
    print()