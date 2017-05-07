from models import Category, Link, Relationship


def list_full():
    print("Categories: ")
    for cat in Category.select():
        print(f" - {cat}")

    print("Links: ")
    for link in Link.select():
        print(f" - {link}")

    print("Relations: ")
    for rel in Relationship.select():
        print(f" - {rel}")


def interactive_create_link():
    title = input("Title: ")
    url = input("URL: ")
    link, created = Link.get_or_create(title=title, url=url)
    if created:
        print("Created!")
    else:
        print("Already existed")


def interactive_create():
    entry_type = input("Type (c/l/r): ")
    if entry_type == "l":
        interactive_create_link()


def print_help():
    print(" - create (alias: c)")
    print(" - list (alias: l)")


def interactive():
    while True:
        cmd = input("> ")
        if cmd.lower() in ["c", "create"]:
            interactive_create()
        elif cmd.lower() in ["l", "list"]:
            list_full()
        elif cmd.lower() in ["h", "help"]:
            print_help()
        else:
            print("Unknown command")
