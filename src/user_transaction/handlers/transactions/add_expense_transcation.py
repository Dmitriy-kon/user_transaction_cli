import argparse


def add_expense_transcation(parser: argparse.ArgumentParser):
    expense_transaction_parser = parser.add_parser(
        "sub", help="расходы"
    )
    expense_transaction_parser.add_argument("username", type=str, help="Имя пользователя")
    expense_transaction_parser.add_argument("money", type=int, help="Количество денег")