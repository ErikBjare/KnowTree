import sys
import logging

import colorama
from colorama import Fore, Style

from ..db.models import Category, Link, Relationship, User, Progress

_msg_created = f"{Fore.GREEN}Created!"
_msg_already_exists = f"{Fore.RED}Already exists"
_msg_unknown_command = f"{Fore.RED}Unknown command"


def list_full():
    for Table in [Category, Link, Relationship, User, Progress]:
        print(f"{Style.BRIGHT}{Table.__name__}: ")
        for item in Table.select():
            print(f" - {item}")


def interactive_create_user():
    username = input("Username: ")
    user, created = User.get_or_create(username=username)
    if created:
        print(_msg_created)
    else:
        print(_msg_already_exists)


def interactive_create_link():
    title = input("Title: ")
    url = input("URL: ")
    link, created = Link.get_or_create(title=title, url=url)
    if created:
        print(_msg_created)
    else:
        print(_msg_already_exists)


def interactive_create():
    entry_type = input("Type (c)ategory/(l)ink/(r)elation/(u)ser: ")
    if entry_type == "l":
        interactive_create_link()
    elif entry_type == "u":
        interactive_create_user()
    else:
        print(f"{entry_type} not supported yet, sorry.")


def print_help():
    print("Available commands:")
    for full, alias in [("create", "c"), ("list", "ls")]:
        print(f" - {Style.BRIGHT}{full}{Style.RESET_ALL} (alias: {alias})")


def _quit():
    print("\nQuitting...")
    sys.exit(0)


def cmd_eval(cmd):
    if cmd.lower() in ["c", "create"]:
        interactive_create()
    elif cmd.lower() in ["ls", "list"]:
        list_full()
    elif cmd.lower() in ["h", "help"]:
        print_help()
    elif cmd.lower() in ["exit"]:
        _quit()
    else:
        print(_msg_unknown_command)


def main():
    colorama.init(autoreset=True)

    if sys.stdin.isatty():
        logging.basicConfig(level=logging.INFO)
        print(f"{Style.BRIGHT}Welcome to the {Fore.GREEN}knowtree{Fore.RESET} CLI!")
        while True:
            try:
                cmd_eval(input(f"{Fore.YELLOW}>{Fore.RESET} "))
            except KeyboardInterrupt:
                print("\nUse command 'exit' or Ctrl+D (EOF) to quit.")
            except EOFError:
                _quit()
    else:
        cmd_eval(input())
