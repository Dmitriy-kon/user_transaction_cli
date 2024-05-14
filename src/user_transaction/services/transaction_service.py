from repositories.transaction_repo import TransactionRepository
from repositories.user_repo import UserRepository


class TransactionService:
    def __init__(self) -> None:
        self.transaction_repo = TransactionRepository()
        self.user_repo = UserRepository()

    def add_transaction(self, name, amount, type_):
        user = self.user_repo.get_user(name)
        if user is None:
            raise ValueError("User not found")
        self.transaction_repo.add_transaction(name, amount, type_)
        

    def get_user_transactions(self, name):
        user = self.user_repo.get_user(name)
        if user is None:
            raise ValueError("User not found")
        
        return self.transaction_repo.get_user_transactions(name)
    
    def get_balans_from_transactions(self, name):
        user = self.user_repo.get_user(name)
        if user is None:
            raise ValueError("User not found")
        
        transactions = self.get_user_transactions(name)
        balans = 0
        if transactions is None:
            return balans
        
        for transaction in transactions:
            if transaction.type_ == "add":
                balans += transaction.amount
            if transaction.type_ == "sub":
                balans -= transaction.amount
                
        return balans

    def close(self):
        self.transaction_repo.close()
        self.user_repo.close()
