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
    
    