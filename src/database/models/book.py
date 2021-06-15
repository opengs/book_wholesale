from tortoise.models import Model
from tortoise.fields.data import IntField, CharField, TextField, DateField

class Book(Model):
    id = IntField(pk=True)
    author = CharField(255, null=False)
    title = CharField(255, null = False)
    description = TextField(null=True)
    publication_date = DateField(null=False)
    info = TextField(null=True)
    price = IntField(null=False)
    count_in_stock = IntField(null=False, default=0)
    discount = IntField(null=True)