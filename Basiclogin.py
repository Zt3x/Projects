
userlist = {    
    "Usernames" : ["Admin", "Some1", "user1"],
    "Passwords" : ["Root", "Something", "paassw0rd"]
}
usernamelist = list(userlist["Usernames"])
passwordlist = list(userlist["Passwords"])
accountquestion  = str(input("Do you have an account? (yes/no)"))
def signup():
    wantedname = str(input("What do you want your username to be ? "))
    wantedpass = str(input("What do you want your password to be ? "))
    usernamelist.append(wantedname)
    userlist["Usernames"] = usernamelist
    passwordlist.append(wantedpass)
    userlist["Password"] = passwordlist

def login():
    givenusername = str(input("What is your username? "))
    givenpassword = str(input("What is your password? "))
    x = usernamelist.index(givenusername)
    if givenusername in usernamelist:
        if passwordlist[x] == givenpassword:
            print("Log in successfull.")
        else:
            print("Wrong Username or Password.")
    else:
        print("Wrong Username or Password.")    

if accountquestion == "no":
    signup()
    print("Your account has been successfully created.")
    login()
elif accountquestion == "yes":
    login()
else:
   print("Invalid input!")
