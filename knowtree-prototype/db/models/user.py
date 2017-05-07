from peewee import CharField, ForeignKeyField, DateTimeField

from . import Model
from . import Link


class User(Model):
    username = CharField()

    def __str__(self):
        return f"<User '{self.username}'>"


class Progress(Model):
    timestamp = DateTimeField()
    user = ForeignKeyField(User, related_name="progress")
    link = ForeignKeyField(Link, related_name="interactions")

    # TODO: What are valid values here?
    # - visited
    # - in-progress
    # - completed
    status = CharField()

    def __str__(self):
        return f"<Progress of {self.user.username} on {self.link.url}: {self.status}>"
