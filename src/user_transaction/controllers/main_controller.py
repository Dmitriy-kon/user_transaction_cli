from argparse import Namespace


from services.user_service import UserService
from services.transaction_service import TransactionService

from presentation.present_transaction import (present_transactions, 
                                              present_user_create,
                                              present_add_transaction,
                                              present_sub_transaction,
                                              present_balans,
                                              present_all_users,
                                              present_delete_user)

def init_controllers(args: Namespace):
    if args.command == "create":
        user_service = UserService()
        user_service.add_user(args.username, args.password)
        present_user_create(args.username)

    if args.command == "delete":
        try:
            user_service = UserService()
            user_service.delete_user(args.username)
            present_delete_user(args.username)
        except ValueError:
            present_delete_user(f"{args.username} not found")
    
    if args.command == "ls":
        user_service = UserService()
        users = user_service.get_all_users()
        present_all_users(users)
    
    if args.command == "transaction":
        if args.transaction_command == "add":
            try:
                transaction_service = TransactionService()
                transaction_service.add_transaction(args.username, args.money, "add")
                present_add_transaction(args.username, args.money)
            except ValueError:
                present_add_transaction(f"{args.username} not found", 0)

        if args.transaction_command == "sub":
            try:
                transaction_service = TransactionService()
                transaction_service.add_transaction(args.username, args.money, "sub")
                present_sub_transaction(args.username, args.money)
            except ValueError:
                present_sub_transaction(f"{args.username} not found", 0)

        if args.transaction_command == "all":
            try:
                transaction_service = TransactionService()
                user_transactions = transaction_service.get_user_transactions(args.username)
                present_transactions(user_transactions)
            except ValueError:
                present_transactions([])
        
        if args.transaction_command == "balans":
            try:
                transaction_service = TransactionService()
                balans = transaction_service.get_balans_from_transactions(args.username)
                present_balans(args.username, balans)
            except ValueError:
                present_balans(f"{args.username} not found", 0)
