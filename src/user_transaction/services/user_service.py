import sqlite3

from repositories.user_repo import UserRepository
from repositories.transaction_repo import TransactionRepository


class UserService:
    def __init__(self) -> None:
        self.user_repo = UserRepository()
        self.transaction_repo = TransactionRepository()

    def get_user_by_name(self, name):
        user = self.user_repo.get_user(name)

        transactions = self.transaction_repo.get_user_transactions(name)

        if transactions is None:
            return user
        user.transactions = transactions

        self.user_repo.close()
        self.transaction_repo.close()

        return user

    def add_user(self, name, hashed_password):
        try:
            self.user_repo.add_user(name, hashed_password)
        except sqlite3.IntegrityError:
            raise ValueError("User with this name already exists")

        self.user_repo.close()
        self.transaction_repo.close()
