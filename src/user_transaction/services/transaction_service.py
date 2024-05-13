from repositories.transaction_repo import TransactionRepository


class TransactionService:
    def __init__(self) -> None:
        self.transaction_repo = TransactionRepository()

    def add_transaction(self, name, amount, type_):
        self.transaction_repo.add_transaction(name, amount, type_)

    def get_user_transactions(self, name):
        return self.transaction_repo.get_user_transactions(name)

    def close(self):
        self.transaction_repo.close()
