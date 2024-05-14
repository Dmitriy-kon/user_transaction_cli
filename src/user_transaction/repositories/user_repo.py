import os
import sqlite3

from adapters.models.models import User


class UserRepository:
    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.connection = sqlite3.connect(f"{self.path}/adapters/user.db")

    def get_user(self, name):
        cursor = self.connection.cursor()
        query = """
            SELECT name, hashed_password FROM users WHERE name = ?
        """
        with self.connection:
            cursor.execute(query, (name,))

        result = cursor.fetchone()
        if result is None:
            return None
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
    
    def delete_user(self, name):
        cursor = self.connection.cursor()
        query = "DELETE FROM users WHERE name = ?"

        with self.connection:
            cursor.execute("PRAGMA foreign_keys = on;")
            
            cursor.execute(
                query,
                (name,),
            )
        self.connection.commit()

    def get_all_users(self):
        cursor = self.connection.cursor()
        query = """
            SELECT name, hashed_password FROM users
        """
        with self.connection:
            cursor.execute(query)

        result = cursor.fetchall()
        if result is None:
            return None

        users = [User(user[0], user[1]) for user in result]
        return users

    def close(self):
        self.connection.close()
