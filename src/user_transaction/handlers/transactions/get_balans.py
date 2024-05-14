import argparse


def get_balans_transcation(parser: argparse.ArgumentParser):
    balans_transaction_parser = parser.add_parser(
        "balans", help="Текущий баланс пользователя"
    )
    balans_transaction_parser.add_argument("username", type=str, help="Имя пользователя")