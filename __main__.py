from knowtree.db import dbinit
from knowtree.cli import main


def run():
    dbinit.db_init()

    main()


def run_rest():
    import app

    app = app.create_app()

    app.run()


if __name__ == "__main__":
    run()
