import argparse


from .users.create_user_pars import create_user_init
from .users.delete_user_pars import delete_user_init
from .users.get_all_users_pars import get_all_users_init

from .transactions.transaction_parser import init_transaction_subparser

def init_main_subparser(parser: argparse.ArgumentParser):
    main_subparser = parser.add_subparsers(dest="command", title="Доступные команды")
    
    create_user_init(main_subparser)
    delete_user_init(main_subparser)
    get_all_users_init(main_subparser)
    
    init_transaction_subparser(main_subparser)
    
    
    
    
    