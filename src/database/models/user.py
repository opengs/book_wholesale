from tortoise.models import Model
from tortoise.fields.data import DatetimeField, IntField, CharField, TextField, DateField
from tortoise.fields.relational import ForeignKeyField

class User(Model):
    id = IntField(pk=True)
    name = CharField(255)
    NIP = CharField(10, null=True)
    address = CharField(255, null=True)
    phone = CharField(20, null=True)
    mail = CharField(32, null=True)