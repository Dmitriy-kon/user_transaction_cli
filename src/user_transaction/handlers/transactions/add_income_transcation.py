import argparse


def add_income_transcation(parser: argparse.ArgumentParser):
    income_transaction_parser = parser.add_parser(
        "add", help="доходы"
    )
    income_transaction_parser.add_argument("username", type=str, help="Имя пользователя")
    income_transaction_parser.add_argument("money", type=int, help="Количество денег")