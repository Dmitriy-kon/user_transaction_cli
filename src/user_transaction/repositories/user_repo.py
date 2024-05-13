import sqlite3

from adapters.models.models import User, Transaction


class UserRepository:
    def __init__(self):
        self.connection = sqlite3.connect("./adapters/user.db")

    # def get_user_with_transaction(self, name):
    #     cursor = self.connection.cursor()
    #     query = """
    #         SELECT users.name, users.hashed_password, transactions.amount, transactions.type FROM users JOIN transactions ON users.name = transactions.name WHERE users.name = ?
    #     """
    #     with self.connection:
    #         cursor.execute(query, (name,))

    #     result = cursor.fetchall()
    #     user = User.from_db(result)
    #     return user
    
    def get_user(self, name):
        cursor = self.connection.cursor()
        query = """
            SELECT name, hashed_password FROM users WHERE name = ?
        """
        with self.connection:
            cursor.execute(query, (name,))

        result = cursor.fetchone()
        user = User(result[0], result[1])
        
        return user
    
    def get_user_transactions(self, name):
        cursor = self.connection.cursor()
        query = """
            SELECT name, amount, type FROM transactions WHERE name = ?
        """
        with self.connection:
            cursor.execute(query, (name,))

        result = cursor.fetchall()
        transactions = [Transaction(row[0], row[1], row[2]) for row in result]
        
        return transactions
    
    def close(self):
        self.connection.close()
        
