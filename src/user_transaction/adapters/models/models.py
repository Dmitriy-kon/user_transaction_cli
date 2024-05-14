from dataclasses import dataclass
from typing import Literal


@dataclass
class User:
    username: str
    hashed_password: str
    transactions: list["Transaction"] | None = None

    @classmethod
    def from_db(cls, result):
        username = result[0][0]
        hashed_password = result[0][1]
        transactions = [Transaction(row[0], row[2], row[3]) for row in result]
        return User(username, hashed_password, transactions)


@dataclass
class Transaction:
    username: str
    amount: int
    type_: Literal["add", "sub"]
