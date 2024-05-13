from dataclasses import dataclass
from typing import Literal


@dataclass
class User:
    id: int
    username: str
    password: str
    transaction: "Transaction"

@dataclass
class Transaction:
    id: int
    username: str
    money: int
    type_: Literal["add", "sub"]
    