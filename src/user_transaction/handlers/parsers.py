import argparse

from .root_parser import init_main_subparser

def init_parsers(parser: argparse.ArgumentParser):
    init_main_subparser(parser)