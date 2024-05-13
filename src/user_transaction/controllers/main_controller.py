from argparse import Namespace


from services.user_service import UserService
from services.transaction_service import TransactionService

from presentation.present_transaction import present_transaction

def init_controllers(args: Namespace):
    if args.command == "create":
        user_service = UserService()
        user_service.add_user(args.username, args.password)

    if args.command == "delete":
        pass
    
    if args.command == "transaction":
        if args.transaction_command == "add":
            transaction_service = TransactionService()
            transaction_service.add_transaction(args.username, args.money, "add")

        if args.transaction_command == "sub":
            transaction_service = TransactionService()
            transaction_service.add_transaction(args.username, args.money, "sub")

        if args.transaction_command == "all":
            transaction_service = TransactionService()
            user_transactions = transaction_service.get_user_transactions(args.username)
            present_transaction(user_transactions)
