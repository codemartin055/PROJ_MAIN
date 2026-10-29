import os
while True:
    f=str(input("Enter name of file here: ")).upper()
    x=True
    y=True
    if os.path.exists(f):
        print("This exists in your computer")
        while x:
            a=str(input("Do you wish to view some or all of its content[All/some]")).upper()
            if a == "SOME":
                with open(f,'r') as file:
                    print(file.readline(50))
                    x=False
            elif a == "ALL":
                with open(f,'r') as file:
                    print(file.read())
                    x=False
            else:
                print("Not a valid option")
        while y:
            b=str(input("Do you wish to delete file(Y/N): ")).upper()
            if b =="Y" or b=="YES":
                os.remove(f)
                print("File deleted")
                y=False
            elif b =="N" or b=="NO":
                print("File retained")
                y=False
            else:
                print("invalid option")  
        
        
