# removes the latest emp

def remEmp():

    fileAppend = open("C:/Users/admin/OneDrive/Desktop/python/Assignments/empPackage/EmpDept.txt","a")
    fileRead = open("C:/Users/admin/OneDrive/Desktop/python/Assignments/empPackage/EmpDept.txt","r")
    data = fileRead.readlines()
    data = data[:-1]
    fileRead.truncate(0)
    fileAppend.writelines(data)