def get_data(file="hw.txt"):
    f=open(file,"+a")
    f.writelines(["\nRoll No : 117","\nName : Shrikant Shedge","\nClass : SYCO-B"])
    print("Reading the File!\n")
    f.seek(0)
    try:
        print(f.readlines())
    except(FileNotFoundError):
        print("File is not yet created!")
    except Exception :
        print(Exception)
get_data()