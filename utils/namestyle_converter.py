import re

from pydantic import BaseModel
from tortoise import Model

from req.EmployeeReq import EmployeeCommon



def underscore_to_camelcase(s):
	parts = s.split('_')
	return parts[0] + ''.join(word.capitalize() for word in parts[1:])


def to_camel(d):  # 暂不支持BaseModel套BaseModel的情况:
	if isinstance(d, BaseModel):
		return to_camel(d.dict())
	elif isinstance(d, dict):
		return {underscore_to_camelcase(k): to_camel(v) for k, v in d.items()}
	elif isinstance(d, list):
		return [to_camel(item) for item in d]
	else:
		return d


def camelcase_to_underscore(s):
	s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()


def to_under(d):
	if isinstance(d, BaseModel):
		return to_under(d.dict())
	elif isinstance(d, dict):
		return {camelcase_to_underscore(k): to_under(v) for k, v in d.items()}
	elif isinstance(d, list):
		return [to_under(item) for item in d]
	else:
		return d


if __name__ == '__main__':
	print(to_camel(EmployeeCommon(id=1, id_number="1", name="hello", phone="1", sex="1", username="user")))
	print(to_under(EmployeeCommon(id=1, id_number="1", name="hello", phone="1", sex="1", username="user")))