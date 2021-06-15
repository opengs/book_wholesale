from tortoise.models import Model
from tortoise.fields.data import DatetimeField, IntField, CharField, TextField, DateField
from tortoise.fields.relational import ForeignKeyField

class Order(Model):
    id = IntField(pk=True)
    date = DatetimeField(null=False)
    info = TextField(null=True)
    user = ForeignKeyField("models.User", "orders")