userlist = {    
    "Usernames" : ["Admin", "Some1", "user1"],
    "Passwords" : ["Root", "Something", "paassw0rd"]
}
usernamelist = list(userlist["Usernames"])
passwordlist = list(userlist["Passwords"])

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

