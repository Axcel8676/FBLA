# will set up the table for the admins accoutns in which 
# will cointain the  id, username and password

import sqlite3 # to create the db
# change the execute for the table 

# this method may only be call by the package
def verify(database:str)->str:
    result = ""
    if database.lower() == "admin":
        result = "databases/admin.db"
    elif database.lower() =="users":
        result = "databases/users.db"
    else:
        print("Couldn't find database")
    return result

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
    #         CREATE TABLE if not exists users
    #         (id INTEGER primary key, userName TEXT, password TEXT)
    #         """
    #     )
    # Note: change later for incript password

    # with will call close and commit auto

#they only need to write admin or users
def add(database:str,*keys):
    "will add an user to the given database"
    addres = verify(database)

    if addres :
        temp = "("
        for i in range(len(keys)):
            if i == len(keys)-1:#meaning we are on the last element
                temp+="?)"
            else:
                temp+="?,"

        with sqlite3.connect(addres) as con:
            cursor = con.cursor()
            if database.lower() == "admin":
                cursor.execute(
                    f"insert into adminUsers values{temp}",
                    keys,
                )
            else:
                cursor.execute(
                    f"insert into users values{temp}",
                    keys,
                )
        # the reason whe put the values after is to prevent 
        # a sql injection that is a way that people use to 
        # stole your data   

#needs db and a tuple that contains strings
def display(database:str,*keys:str):
    """
    Will give the data from the given databse,
    it accepts the arguments that want to be 
    display like id, name 
    """
    addres =  verify(database)
    if addres:
        with sqlite3.connect(addres) as con:
            cursor = con.cursor()
            if database.lower() == "admin":
                cursor.execute(f"SELECT {keys} from adminUsers")
            else:
                cursor.execute(f"SELECT {keys} from users")
            temp = cursor.fetchall()#will return all the data that has that specifications
            for i in len(keys):
                for a in temp:
                    #will print each requested data
                    print(keys[i]+": ",a[i])#may return an error



def searchId(database:str,id:int)->tuple:#returns tuple because will only return one user/admin
    "will search the user/admin from the given id"
    addres =verify(database)
    if addres:
        with sqlite3.connect(addres) as con:
            cursor = con.cursor()
            if database.lower()== 'admin':
                cursor.execute(f"SELECT {id} from adminUsers")
                return cursor.fetchone()
            else:
                cursor.execute(f"SELECT {id} from users")
                return cursor.fetchone()
        
# bacuse is look by name could return a lot of list cointaing each the keys of each user/admin
# admins Must not have the same userName
# will return list of tuples 
def searchName(database:str, name:str)->list:
    "will search the user/admin from the given name"
    addres =verify(database)
    if addres:
        with sqlite3.connect(addres) as con:
            cursor = con.cursor()
            if database.lower()== 'admin':
                cursor.execute(f"SELECT {name} from adminUsers")
                return cursor.fetchall()
            else:
                cursor.execute(f"SELECT {name} from users")
                return cursor.fetchall()

            
def delete(database:str,userid:int):
    "Will delete a user from the given database"
    
    pass