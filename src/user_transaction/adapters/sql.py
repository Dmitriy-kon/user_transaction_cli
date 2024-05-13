import sqlite3


from models.models import User, Transaction

connection = sqlite3.connect("src/user_transaction/adapters/user.db")


def create_table(connection: sqlite3.Connection):
    cursor = connection.cursor()
    with open(
        "src/user_transaction/adapters/sqls/create_transactions.sql", "r"
    ) as f, open("src/user_transaction/adapters/sqls/create_user.sql", "r") as g:
        cursor.executescript(f.read())
        cursor.executescript(g.read())
    connection.commit()


def add_user(connection: sqlite3.Connection, name, hashed_password):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (name, hashed_password) VALUES (?, ?)",
        (name, hashed_password),
    )
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





def add_transaction(connection: sqlite3.Connection, name, amount, type_):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO transactions (name, amount, type) VALUES (?, ?, ?)",
        (name, amount, type_),
    )
    connection.commit()


create_table(connection)


add_user(connection, "test", "testpassword")
add_user(connection, "test2", "testpassword")
add_user(connection, "test3", "testpassword")

add_transaction(connection, "test", 100, "add")
add_transaction(connection, "test", 300, "sub")
add_transaction(connection, "test2", 300, "sub")

user = get_user_with_transaction(connection, "test")
user2 = get_user_with_transaction(connection, "test2")
# user2 = get_user(connection, "test3")

print(user, type(user))
print(user2, type(user))

connection.cursor().execute("DROP TABLE transactions;")
connection.cursor().execute("DROP TABLE users;")
connection.close()
