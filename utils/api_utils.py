from models.GeneralModel import GeneralModel
from utils.namestyle_converter import camelcase_to_underscore


def copyattr(source, target, converter=camelcase_to_underscore):
	# 遍历源对象的属性
	for attr in dir(source):
		# 如果属性是方法或私有属性，则跳过
		if attr.startswith('__') or attr.startswith('_') or callable(getattr(source, attr)):
			continue
		# 如果目标对象也有这个属性，则复制它
		new_attr = converter(attr) if converter else attr
		if hasattr(target, new_attr):
			setattr(target, new_attr, getattr(source, attr))
	return target


def _get_update_entries(obj: GeneralModel):
	return {k: v for k, v in dict(obj).items() if k != "id" and v is not None and v != ""}


async def update_by_id(obj: GeneralModel):
	cls = obj.__class__
	await cls.filter(id=obj.id).update(**_get_update_entries(obj))


async def get_offset(page: int, pageSize: int):
	return (page - 1) * pageSize
