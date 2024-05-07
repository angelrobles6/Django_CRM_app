# This code is used to create a sample database.

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

con = psycopg2.connect(
    user='postgres',
    host='localhost',
    password='test$erv3r'
)

print("Creating Database ...")

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

cur = con.cursor()

# Use the psycopg2.sql module instead of string concatenation
# in order to avoid sql injection attacks.
cur.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier('foocompany'))
    )

print("Database Created Successfully!")

