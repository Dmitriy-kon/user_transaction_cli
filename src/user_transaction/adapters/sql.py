import os
import sqlite3


def create_table():
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(f"{path}/user.db")
    cursor = connection.cursor()

    with open(f"{path}/sqls/create_transactions.sql", "r") as f, open(
        f"{path}/sqls/create_user.sql", "r"
    ) as g:
        cursor.executescript(f.read())
        cursor.executescript(g.read())
    connection.commit()


def drop_tables():
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(f"{path}/user.db")
    
    connection.cursor().execute("DROP TABLE transactions;")
    connection.cursor().execute("DROP TABLE users;")
    connection.close()
