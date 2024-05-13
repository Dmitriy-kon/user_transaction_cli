from .text_formatter import format_text_no_transactions, format_text_all_transactions

from adapters.models.models import Transaction


def present_transaction(transactions: list[str] | None = None):
    if transactions is None:
        text = "No transactions"
        format_text_no_transactions(text)
        return
    format_text_all_transactions(transactions)
