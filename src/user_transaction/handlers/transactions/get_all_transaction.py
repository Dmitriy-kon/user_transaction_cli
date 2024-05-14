import argparse


def all_transcation(parser: argparse.ArgumentParser):
    all_transaction_parser = parser.add_parser(
        "all", help="Все транзакции пользователя"
    )
    all_transaction_parser.add_argument("username", type=str, help="Имя пользователя")