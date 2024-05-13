import os
import sqlite3


from adapters.models.models import User, Transaction

# connection = sqlite3.connect("src/user_transaction/adapters/user.db")
path = os.path.dirname(os.path.abspath(__file__))


def create_table(connection: sqlite3.Connection):
    cursor = connection.cursor()
    with open(
        f"{path}/sqls/create_transactions.sql", "r"
    ) as f, open(f"{path}/sqls/create_user.sql", "r") as g:
        cursor.executescript(f.read())
        cursor.executescript(g.read())
    connection.commit()



def get_user_with_transaction(connection: sqlite3.Connection, username):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT users.name, users.hashed_password, transactions.amount, transactions.type FROM users JOIN transactions ON users.name = transactions.name WHERE users.name = ?",
        (username,),
    )
    result = cursor.fetchall()

    # transactions = [Transaction(row[0], row[2], row[3]) for row in result]
    
    # user = User(result[0][0], result[0][1], transactions)
    user = User.from_db(result)

    return user

def drop_tables(connection):
    connection.cursor().execute("DROP TABLE transactions;")
    connection.cursor().execute("DROP TABLE users;")
    connection.close()
