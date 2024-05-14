import argparse


def get_all_users_init(parser: argparse.ArgumentParser):
    parser.add_parser("ls", help="Показать всех пользователей")
    # get_all_users_parser = parser.add_parser("create", help="Создать пользователя")
    # get_all_users_parser.add_argument("username", type=str, help="Имя пользователя")
