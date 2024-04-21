user = input("Enter your Password : ")
j=0
k=0
l=0
if len(user) >= 8 : 
    if user[0].isalpha():
        if "@" in user and user.count("@") == 1 :
            if "." in user and user.count(".") == 1 and (user[-4] == "." or user[-3]==".") :
                for i in user :
                    if i == i.isspace :
                        j=1
                    elif i.isalpha :
                        if i == i.upper():
                            k=1
                    elif i == "." or i == "@" or i == "_" :
                        continue
                    elif i.isdigit:
                        continue
                    else :
                        l=1 
                if (j == 1) or (k ==1) or (l == 1) :
                    print("wrong email5")    
            else :
                print("wrong email4")
        else :
            print("wrong email3")
    else :
        print("wrong email2")
else :
    print("wrong email1")
