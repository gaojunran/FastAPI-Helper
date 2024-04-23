import logging

from models.GeneralModel import GeneralModel
from utils.namestyle_converter import camelcase_to_underscore


def copyattr(source,
			 target,
			 converter=camelcase_to_underscore,
			 skip: list | tuple = (),
			 debug_mode: bool = False  # 仅在开发环境下开启，以日志形式展示拷贝成功的键值对
			 ):
	success_copies = {}
	# 遍历源对象的属性
	for attr in dir(source):
		# 如果属性是方法或私有属性，则跳过
		if attr.startswith('__') or attr.startswith('_') or callable(getattr(source, attr)):
			continue
		# 如果目标对象也有这个属性，则复制它
		new_attr = converter(attr) if converter else attr
		if hasattr(target, new_attr) and new_attr not in skip:
			setattr(target, new_attr, getattr(source, attr))
			success_copies[new_attr] = getattr(source, attr)
	logging.info(success_copies) if debug_mode else None
	return target


def _get_update_entries(obj: GeneralModel, skip: list | tuple = ()):
	return {k: v for k, v in dict(obj).items() if k != "id" and k not in skip and v is not None and v != ""}


async def update_by_id(obj: GeneralModel, skip: list | tuple = ()):
	cls = obj.__class__
	await cls.filter(id=obj.id).update(**_get_update_entries(obj, skip=skip))


async def get_offset(page: int, pageSize: int):
	return (page - 1) * pageSize


def changeattr(old: str, new: str):
	return None
