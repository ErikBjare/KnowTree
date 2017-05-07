from db import dbinit, interpreter


def run():
    print("Running...")
    dbinit.db_init()

    interpreter.interactive()


def run_rest():
    import app

    app = app.create_app()

    app.run()


if __name__ == "__main__":
    run()
