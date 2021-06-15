from tortoise.models import Model
from tortoise.fields.data import IntField
from tortoise.fields.relational import ForeignKeyField

class OrderDetails(Model):
    order = ForeignKeyField("models.Order", "details")
    book = ForeignKeyField("models.Book", "orders")
    count = IntField()
    total_price = IntField()

    class Meta:
        unique_together=(("order", "book"), )