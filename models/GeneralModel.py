from tortoise import fields
from tortoise.models import Model


class GeneralModel(Model):
	create_time = fields.DatetimeField(auto_now_add=True)
	update_time = fields.DatetimeField(auto_now=True)
	create_user = fields.IntField()
	update_user = fields.IntField()
