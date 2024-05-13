import argparse
import sqlite3

import os


from adapters.sql import create_table, drop_tables

from services.user_service import UserService


from handlers.parsers import init_parsers

path = os.path.dirname(os.path.abspath(__file__))

# create_table(sqlite3.connect(f"{path}/adapters/user.db"))


def add_user():
    user_service = UserService()
    user_service.add_user("test", "testpasswor21")


def get_user_by_name():
    user_service = UserService()
    user = user_service.get_user_by_name("test")
    return user


def main():
    parser = argparse.ArgumentParser(
        "Обработчик транзакции пользователя", add_help=True
    )
    init_parsers(parser)
    args = parser.parse_args()


if __name__ == "__main__":
    main()


# args = parser.parse_args()

# if args.command == "create":
#     print(f"{args.username} create")
# if args.command == "delete":
#     print(f"{args.username} delete")
# if args.command == "transaction":
#     print(f"{args.username} transaction")
#     if args.transaction_command == "add":
#         print(f"{args.username} add {args.money}")
#     if args.transaction_command == "sub":
#         print(f"{args.username} sub {args.money}")

# parser.add_argument("transaction_id", type=int, help="ID транзакции")
# parser.add_argument("transaction_type", type=str, help="Тип транзакции")
