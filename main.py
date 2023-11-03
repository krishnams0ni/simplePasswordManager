from dataOps import *
from userOps import *
from encryption import *

i = int(input("1. Login\n2. Register\n3. Remove user\n"))
if i == 1:
    username = input("Username: ")
    password = input("Password: ")
    s = loginPortal(username, password)
    if s:
        print("Welcome!")
    else:
        print("Invalid credentials.")
        exit()

    i = 0
    while i != 4:
        try:
            i = int(input("1. View data\n2. Add Site\n3. Remove Site\n4. Quit\n"))
        except:
            print("Invalid input.")
        if i == 1:
            info = userInfo(username)
            for i in info:
                print(decrypt(i[0]), ":", decrypt(i[1]))

        elif i == 2:
            site = input("Site name: ")
            site_password = input("Site Password: ")
            print(addSite(username, site, site_password))
        elif i == 3:
            print(removeSite(username, input("Site name: "), input("Site Password: ")))

elif i == 2:
    name = input("Name: ")
    username = input("Username: ")
    password = input("Password: ")
    confirmPassword = input("Confirm Password: ")
    email = input("Email: ")
    print(addUser(name, username, password, confirmPassword, email))

elif i == 3:
    username = input("Username: ")
    password = input("Password: ")
    if "Yes" == input("Are you sure? ('Yes' to confirm) "):
        print(removeUser(username, password))
    else:
        print("Action cancelled.")
