from tortoise.models import Model
from tortoise.fields.data import DatetimeField, IntField, CharField, TextField, DateField
from tortoise.fields.relational import ForeignKeyField

class User(Model):
    user = ForeignKeyField("models.User", "system_user", pk=True)
    login = CharField(255, null=False)
    password = CharField(255, null=False)