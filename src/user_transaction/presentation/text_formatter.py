from .color_formater import ColorFormat

from adapters.models.models import Transaction

def format_text_no_transactions(text: str):
    color_format = ColorFormat()
    
    size = len(text) + 4
    text = color_format.red("No transactions")
        
    print(size * "-")
    print(f"| {text} |")
    print(size * "-")

def format_text_all_transactions(transactions: list[Transaction]):
    color_format = ColorFormat()
    
    if len(transactions) == 0:
        text = "No transactions"
        size = len(text) + 4
        text = color_format.red(f"{text}")
        print(size * "-")
        print(f"| {text} |")
        print(size * "-")
        return
    
    name = transactions[0].username.title()
    firts = "| Количество |    Тип     |"
    size = len(firts)

    print(size * "-")
    print(f"|{name.center(size-2)}|")
    print(firts)
    print(f"|{(size-2) * "-"}|")
    for transaction in transactions:
        if transaction.type_ == "add":
            type_ = color_format.green("Прибыль")
        else:
            type_ = color_format.red("Убыток")
        
        print(f"|{str(transaction.amount).center(12)}|{type_.center(22)}|")
    print(size * "-")
    

def format_text_create_user(text: str):
    color_format = ColorFormat()
    
    text = f"{text.title()} created"
    size = len(text) + 4
    text = color_format.green(f"{text}")
        
    print(size * "-")
    print(f"| {text} |")
    print(size * "-")

def format_text_add_transaction(text: str):
    color_format = ColorFormat()
    
    text = text.title()
    size = len(text) + 4
    text = color_format.green(f"{text}")
        
    print(size * "-")
    print(f"| {text} |")
    print(size * "-")


def format_text_sub_transaction(text: str):
    color_format = ColorFormat()
    
    text = text.title()
    size = len(text) + 4
    text = color_format.red(f"{text}")
        
    print(size * "-")
    print(f"| {text} |")
    print(size * "-")

def format_balans(name: str, balans: int):
    color_format = ColorFormat()
    text = f"{name} balans {balans}"
    size = len(text) + 4
    text = color_format.yellow(text)
    
    print(size * "-")
    print(f"| {text} |")
    print(size * "-")

def format_all_users(users: list):
    color_format = ColorFormat()
    
    text = "All users"
    size = len(text) + 4
    text = color_format.green(text)
    
    print(size * "-")
    print(f"| {text} |")
    print(size * "-")
    
    for user in users:
        user_text = color_format.yellow(user.username.title().center(size-4))
        print(f"| {user_text} |")
    
    print(size * "-")
    
def format_delete_user(name: str):
    color_format = ColorFormat()
    
    text = f"{name} deleted"
    size = len(text) + 4
    text = color_format.red(text)
    
    print(size * "-")
    print(f"| {text} |")
    print(size * "-")