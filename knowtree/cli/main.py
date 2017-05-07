import sys

from ..db.models import Category, Link, Relationship, User, Progress


def list_full():
    for Table in [Category, Link, Relationship, User, Progress]:
        print(f"{Table.__name__}: ")
        for item in Table.select():
            print(f" - {item}")


def interactive_create_user():
    username = input("Username: ")
    user, created = User.get_or_create(username=username)
    if created:
        print("Created!")
    else:
        print("Already existed")


def interactive_create_link():
    title = input("Title: ")
    url = input("URL: ")
    link, created = Link.get_or_create(title=title, url=url)
    if created:
        print("Created!")
    else:
        print("Already existed")


def interactive_create():
    entry_type = input("Type (c)ategory/(l)ink/(r)elation/(u)ser: ")
    if entry_type == "l":
        interactive_create_link()
    elif entry_type == "u":
        interactive_create_user()
    else:
        print(f"{entry_type} not supported yet, sorry.")


def print_help():
    print(" - create (alias: c)")
    print(" - list (alias: l)")


def _quit():
    print("\nQuitting...")
    sys.exit(0)


def _loop():
    cmd = input("> ")
    if cmd.lower() in ["c", "create"]:
        interactive_create()
    elif cmd.lower() in ["l", "list"]:
        list_full()
    elif cmd.lower() in ["h", "help"]:
        print_help()
    elif cmd.lower() in ["exit"]:
        _quit()
    else:
        print("Unknown command")


def main():
    while True:
        try:
            _loop()
        except KeyboardInterrupt:
            print("\nUse command 'exit' or Ctrl+D (EOF) to quit.")
        except EOFError:
            _quit()
