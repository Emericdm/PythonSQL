# # Using PostgreSQL in Python (with Psycopg2)
# 
# ### Psycopg2
# 
# A library that allows Python to connect to an existing PostgreSQL database to utilize SQL functionality.

import psycopg2 as pg2

# Create a connection with PostgreSQL
# 'password' is whatever password you set in the install 
conn = pg2.connect(database='postgres', user='postgres',password='password')

# Establish connection and start cursor to be ready to query
cur = conn.cursor()

# Pass in a PostgreSQL query as a string
cur.execute("SELECT * FROM payment")

# Return a tuple of the first row as Python objects
cur.fetchone()

# Return N number of rows
cur.fetchmany(10)

# Return All rows at once
cur.fetchall()

# To save and index results, assign it to a variable
data = cur.fetchmany(10)

# **Inserting Information**

query1 = '''
        CREATE TABLE new_table (
            userid integer
            , tmstmp timestamp
            , type varchar(10)
        );
        '''
cur.execute(query1)

# commit the changes to the database
cur.commit()

# Don't forget to close the connection!
# killing the kernel or shutting down juptyer will also close it
conn.close()

