from .text_formatter import (format_text_no_transactions, 
                             format_text_all_transactions,
                             format_text_create_user,
                             format_text_add_transaction,
                             format_text_sub_transaction
                             )

from adapters.models.models import Transaction


def present_transactions(transactions: list[str] | None = None):
    if transactions is None:
        text = "No transactions"
        format_text_no_transactions(text)
        return
    format_text_all_transactions(transactions)


def present_user_create(name: str):
    format_text_create_user(name)

def present_add_transaction(username: str, amount: int):
    text = f"{username} added {amount}"
    format_text_add_transaction(text)

def present_sub_transaction(username: str, amount: int):
    text = f"{username} sub {amount}"
    format_text_sub_transaction(text)