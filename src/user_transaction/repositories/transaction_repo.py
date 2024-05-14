import os
import sqlite3

from adapters.models.models import Transaction


class TransactionRepository:
    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.connection = sqlite3.connect(f"{self.path}/adapters/user.db")


    def add_transaction(self, name, amount, type_):
        cursor = self.connection.cursor()
        query = "INSERT INTO transactions (name, amount, type) VALUES (?, ?, ?)"

        with self.connection:
            cursor.execute(
                query,
                (name, amount, type_),
            )
        self.connection.commit()

    def get_user_transactions(self, name):
        cursor = self.connection.cursor()
        query = """
            SELECT name, amount, type FROM transactions WHERE name = ?
        """
        with self.connection:
            cursor.execute(query, (name,))

        result = cursor.fetchall()
        if not result:
            return None
        transactions = [Transaction(row[0], row[1], row[2]) for row in result]

        return transactions

    def close(self):
        self.connection.close()
