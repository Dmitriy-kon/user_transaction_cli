import argparse


def create_user_init(parser: argparse.ArgumentParser):
    create_user_parser = parser.add_parser("create", help="Создать пользователя")
    create_user_parser.add_argument("username", type=str, help="Имя пользователя")
