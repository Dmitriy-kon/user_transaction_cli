import os
import sqlite3

from adapters.models.models import User


class UserRepository:
    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        self.connection = sqlite3.connect(f"{self.path}/adapters/user.db")

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

    def add_user(self, name, hashed_password):
        cursor = self.connection.cursor()
        query = "INSERT INTO users (name, hashed_password) VALUES (?, ?)"

        with self.connection:
            cursor.execute(
                query,
                (name, hashed_password),
            )
        self.connection.commit()

    def close(self):
        self.connection.close()
