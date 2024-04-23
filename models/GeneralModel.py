from tortoise import fields
from tortoise.models import Model


# def auto_setter(cls):
# 	for attr_name in cls.__dict__:
# 		if not attr_name.startswith('__'):
# 			attr_value = getattr(cls, attr_name)
# 			setattr(cls, attr_name,
# 					property(attr_value, lambda self, value, name=attr_name: setattr(self, f"_{name}", value)))
# 	return cls


# @auto_setter
class GeneralModel(Model):
	create_time = fields.DatetimeField(auto_now_add=True)
	update_time = fields.DatetimeField(auto_now=True)
	create_user = fields.IntField()
	update_user = fields.IntField()
