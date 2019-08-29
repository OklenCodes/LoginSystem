users = {}
status = ""

def displayMenu():
    status = input("Are you a registered user? Y/N? press Q to quit")
    if status == "Y":
        oldUser()
    elif status == "N":
        newUser()
def newUser():
    createlogin = input("Create Login name: ")
    if createlogin in users:
        print("\nLogin name already exists!\n")
    else:
        createPassword = input("Create Password: ")
        users[createlogin] = createPassword
        print("\nUser created\n")


def oldUser():
    login = input("Enter Login name: ")
    password = input("Enter Password: ")
    if login in users and users[login] == password:
        print("\nLogin Successful!\n""\nWelcome back Mr Stark\n")
    else:
        print ("\nLogin/Password combination incorrect!\n")
        counter = 1
        print("Attempts left:", counter)

while status != "Q":
    displayMenu()

#May add things such as password must contain numbers capitals etc. And a password failure count.