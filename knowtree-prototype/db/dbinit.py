from datetime import datetime, timezone

from . import database
from .models import Category, Link, Relationship, User, Progress


cat_math = None
link_ka = None


def db_init():
    database.connect()

    if not database.get_tables():
        database.create_tables([Category, Link, Relationship, User, Progress], True)
        print(f"Tables created: {database.get_tables()}")

        _create_example_graph()
    else:
        print("Database was already initalized")


def _create_example_graph():

    """
    Build knowtree.
    """
    _create_math_cat()
    _create_math_links()

    cat_algebra, created = Category.get_or_create(title="Calculus", supercat=cat_math)
    if not created:
        print("Created Calculus category")

    """
    Create some user activity.
    """
    user = _create_example_user()
    _create_example_progress(user)


def _create_math_cat():
    global cat_math
    cat_math, created = Category.get_or_create(title="Mathematics")
    return cat_math


def _create_math_links():
    global link_ka
    link_ka, created = Link.get_or_create(title="Khan Academy", url="https://khanacademy.org/")
    rel, created = Relationship.get_or_create(from_category=cat_math, to_link=link_ka)


def _create_example_user():
    user, created = User.get_or_create(username="erb")
    return user


def _create_example_progress(user):
    progress_data = [Progress(user=user, link=link_ka, status="in-progress", timestamp=datetime.now(timezone.utc))]

    for prog in progress_data:
        item = Progress.select().where(Progress.user == prog.user and \
                                       Progress.link == prog.link and \
                                       Progress.status == prog.status)
        if not item:
            prog.save()
