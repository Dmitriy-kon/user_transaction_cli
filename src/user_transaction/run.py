import argparse

import os


from adapters.sql import create_table, drop_tables


from handlers.parsers import init_parsers
from controllers.main_controller import init_controllers

path = os.path.dirname(os.path.abspath(__file__))


def main():
    parser = argparse.ArgumentParser(
        "Обработчик транзакции пользователя", add_help=True
    )
    init_parsers(parser)
    args = parser.parse_args()

    init_controllers(args)


if __name__ == "__main__":
    # drop_tables()
    create_table()
    main()
