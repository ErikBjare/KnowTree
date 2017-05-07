from peewee import Model as BaseModel
from peewee import SqliteDatabase, CharField, TextField, PrimaryKeyField, ForeignKeyField


DATABASE = "loltest.sqlite"
database = SqliteDatabase(DATABASE)


class Model(BaseModel):
    class Meta:
        database = database


# TODO: We need a way to get a list of links that belong to a specific category or at least one of its child categories.
class Category(Model):
    """This is a knowledge category. It currently has a tree structure but might be made a DAG later."""
    title = CharField(index=True, unique=False)
    description = TextField(null=True)
    supercat = ForeignKeyField('self', null=True, related_name="subcategories")  # supercat ftw.

    def __str__(self):
        return f"<{self.title}>"


class Link(Model):
    """Represents a learning resource"""
    title = CharField(index=True)
    # FIXME: Should this be of another field type?
    url = CharField(index=True)

    def __str__(self):
        return f"<{self.title} @ {self.url}>"


class Relationship(Model):
    from_category = ForeignKeyField(Category, related_name='links')
    to_link = ForeignKeyField(Link, related_name='categories')

    class Meta:
        indexes = (
            # Specify a unique multi-column index on from/to-user.
            (('from_category', 'to_link'), True),
        )

    def __str__(self):
        return f"<{self.from_category} -> {self.to_link}>"
