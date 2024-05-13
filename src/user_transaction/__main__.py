import argparse



parser = argparse.ArgumentParser("Обработчик транзакции пользователя", add_help=True)


main_subparser = parser.add_subparsers(dest="command", title="Доступные команды")


# Создать пользователя
create_user_parser = main_subparser.add_parser("create", help="Создать пользователя")
create_user_parser.add_argument("username", type=str, help="Имя пользователя")

# Удалить пользователя
delete_user_parser = main_subparser.add_parser("delete", help="Удалить пользователя")
delete_user_parser.add_argument("username", type=str, help="Имя пользователя")


# Транзакции
transaction_parser = main_subparser.add_parser("transaction", help="Транзакция пользователя")

# Команды транзакции
transaction_subparser = transaction_parser.add_subparsers(dest="transaction_command", help="Команды транзакции")

# Доходы
income_transaction_parser = transaction_subparser.add_parser("add", help="доходы")
income_transaction_parser.add_argument("username", type=str, help="Имя пользователя")
income_transaction_parser.add_argument("money", type=int, help="Количество денег")

# Расходы
expense_transaction_parser = transaction_subparser.add_parser("sub", help="расходы")
expense_transaction_parser.add_argument("username", type=str, help="Имя пользователя")
expense_transaction_parser.add_argument("money", type=int, help="Количество денег")

# Все транзакции пользователя
all_transactions_parser = transaction_subparser.add_parser("all", help="Все транзакции пользователя")
all_transactions_parser.add_argument("username", type=str, help="Имя пользователя")








args = parser.parse_args()

if args.command == "create":
    print(f"{args.username} create")
if args.command == "delete":
    print(f"{args.username} delete")
if args.command == "transaction":
    print(f"{args.username} transaction")
    if args.transaction_command == "add":
        print(f"{args.username} add {args.money}")
    if args.transaction_command == "sub":
        print(f"{args.username} sub {args.money}")

# parser.add_argument("transaction_id", type=int, help="ID транзакции")
# parser.add_argument("transaction_type", type=str, help="Тип транзакции")

