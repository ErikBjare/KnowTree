import models
import interpreter


def run():
    print("Running...")
    models.db_init()

    models.create_example_graph()

    interpreter.interactive()


if __name__ == "__main__":
    run()
