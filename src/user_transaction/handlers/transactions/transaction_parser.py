import argparse

from .add_income_transcation import add_income_transcation
from .add_expense_transcation import add_expense_transcation
from .get_all_transaction import all_transcation

def init_transaction_subparser(parser: argparse.ArgumentParser):
    transaction_parser = parser.add_parser(
        "transaction", help="Транзакция пользователя"
    )
    transaction_subparser = transaction_parser.add_subparsers(
        dest="transaction_command", help="Команды транзакции"
    )

    add_income_transcation(transaction_subparser)
    add_expense_transcation(transaction_subparser)
    all_transcation(transaction_subparser)
    