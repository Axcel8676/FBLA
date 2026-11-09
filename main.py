#Serving the Community: Nonprofit Volunteer Management
# Nonprofit organizations rely on volunteers to support programs, events, and community initiatives.
# Effectively managing volunteer information, service opportunities, schedules, and participation can
# help organizations operate more efficiently and increase their impact.

# Use your programming skills to develop a program that helps nonprofit organizations recruit, organize,
# and manage volunteers and community service activities. Your program may be a command-line
# application, desktop application, or interactive interface. Choose the platform that best demonstrates
# your programming skills.
# Your solution should help nonprofit organizations coordinate volunteers, manage service
# opportunities, maintain records, and monitor participation while supporting the needs of both
# volunteers and organization leaders

# task 1: set up data base in which is going to be store the users to sign in(the admins) 
# done^

# task 2: set up the command line application in which the firts thing is to ask for sign in or create account
# task 3: set up a menu in which they could interact more friendly depending on what they want to do
from databases import dbFunctions
from msj import commands

dbFunctions.start()
sigin = False

def sigIn()->bool:
    sigin = False
    comand = input("Comand: ")
    
    if(comand.lower() == "s"):#Sigin
        userName = input("User: ")
        dbFunctions.searchName("admin",userName)
        # for the moment skip no password 
        sigin = True
    
    elif(comand.lower()== "c"):#Create
        adminUser = input("Please enter a Username for the account: ")
        # needs yo verify that User hasn't been selected
        password = input("Please enter the password: ")
        dbFunctions.add("admin",adminUser,password)
        print("All set please sig in to continue")
        sigin = True

    return sigin

while(True):
    print(commands.initialOp)
    if sigIn():#to verify the admin has a account
        while(True):
            print("You are in")
            holder = input("Command: ")
    else:
        print("Error please try again")