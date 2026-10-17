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

dbFunctions.start()
sigin = False

# create a directory for the msj
msj = """ 
Welcome plese write: 
sigin if have an account
create if don't have an account

"""

while(True):
    if sigin:#to verify the admin has a account
        print(msj)
        comand = input("Comand: ")
        if(comand.lower() == "sigin"):
            userName = input("User: ")
            dbFunctions.searchName("admin",userName)
        elif(comand.lower()== "create"):
            pass
        else:
            print("Wrong command please try again")
    else:
        pass