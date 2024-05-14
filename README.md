### Transactions
Приложение по работе с финансами.

Может обслуживать несколько пользователей. Имеет 2 вида транзакций: прибыль и убыток.

#### Commands:
  
- create: Создание пользователя с паролем `user_transaction create oleg 58`
- delete: Удаление пользователя и всех его транзакций `user_transaction delete oleg`
- ls: Показывает всех пользователей

- transaction: Позволяет работать с транзакциями
	- add: Добавляет прибыль для пользователя `user_transaction transaction add oleg 200`
	-  sub: Добавляет убыток для пользователя `user_transaction transaction sub oleg 200`
	-  all: Показывает все транзакции пользователя `user_transaction transaction all oleg`
	-  balans: Показывает нынешний баланс пользователя `user_transaction transaction balans oleg`