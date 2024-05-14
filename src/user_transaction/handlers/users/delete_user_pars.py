import argparse


def delete_user_init(parser: argparse.ArgumentParser):
    delete_user_parser = parser.add_parser("delete", help="Удалить пользователя")
    delete_user_parser.add_argument("username", type=str, help="Имя пользователя")
