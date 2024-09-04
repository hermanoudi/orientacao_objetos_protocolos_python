import sqlite3

con = sqlite3.connect("sql_example.db")

sql = """\
    CREATE TABLE if not exists person(
        id integer PRIMARY KEY AUTOINCREMENT,
        name varchar,
        email varchar UNIQUE NOT NULL,
        dept varchar,
        role varchar
    )
"""
con.execute(sql)

# con.commit()
con.close()
