# will set up the table for the admins accoutns in which 
# will cointain the  id, username and password

import sqlite3 # to create the db


def start():#Must call at the begin
    "will start the databases if not exist"
    # to connect us with the data base 
    with sqlite3.connect("databases/admin.db") as con:# will cointain the admins accounts
        cursor = con.cursor()
        # Will create a table containing the id, username and password
        cursor.execute(
            """
            CREATE TABLE if not exists adminUsers
            (id INTEGER primary key, userName TEXT, password TEXT)
            """
            )

    # execute later 
    # with sqlite3.connect("databases/users.db") as con:
    #     cursor = con.cursor()
    #     cursor.execute(
    #         """
    #         CREATE TABLE if not exists adminUsers
    #         (id INTEGER primary key, userName TEXT, password TEXT)
    #         """
    #     )
    # Note: change later for incript password

    # with will call close and commit auto

#they only need to write admin or user
def add(database:str,*keys):
    "will add an user to the given database"
    addres = ""

    if database.lower() == "admin":
        addres = "databases/admin.db"
    elif database.lower() =="users":
        addres = "databases/users.db"
    else:
        print("Couldn't find database")
        
    if addres :
        temp = "("
        for i in range(len(keys)):
            if i == len(keys)-1:#meaning we are on the last element
                temp+="?)"
            else:
                temp+="?,"

        with sqlite3.connect(addres) as con:
            cursor = con.cursor()
            cursor.execute(
                f"insert into usuarios values{temp}",
                keys,
            )
        # the reason whe put the values after is to prevent 
        # a sql injection that is a way that people use to 
        # stole your data   

#needs db and a tuple that contains strings
def display(database:str,*keys:str):
    """
    Will the data from the given databse,
    it accepts the arguments that want to be 
    display
    """
    addres = ""
    
    if database.lower() == "admin":
        addres = "databases/admin.db"
    elif database.lower() =="users":
        addres = "databases/users.db"
    else:
        print("Couldn't find database")
            
    if addres:
        with sqlite3.connect(addres) as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT {keys} from usuarios")
            temp = cursor.fetchall()#will return all the data that has that specifications
            for i in len(keys):
                for a in temp:
                    #will print each requested data
                    print(keys[i]+": ",a[i])

def delete(database:str,userid:int):
    "Will delete a user from the given database"
    
    pass