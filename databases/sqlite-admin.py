# will set up the table for the admins accoutns in which 
# will cointain the  id, username and password

import sqlite3 # to create the db

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
# Note: change later for incript password

# with will call close and commit auto