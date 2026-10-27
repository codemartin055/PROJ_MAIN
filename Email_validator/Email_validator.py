
def EmailVal(address):
    has_cap=False
    dot = address.find(".")
    at = address.find("@")
    if (dot == -1):
        print("Invalid no '.' found")
        exit()
    elif (at == -1):
        print("Invalid no '@' found ")
        exit()
    elif  has_cap==False:
        for i in address:
                if i.isupper():
                        has_cap=True
                        break
        if has_cap:
           print("the word given has atleast a capital letter in it")
        else:
            print("your Email is Valid")

print("This program will decide if your input is a valid email address")
while(True):
    print("A valid email address needs an '@' symbol and a '.' and no capital letters")
    x = input("Input your email address:")

    EmailVal(x)