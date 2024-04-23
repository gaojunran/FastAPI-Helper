from dataclasses import dataclass

from settings import API
from utils.namestyle_converter import to_camel


@dataclass
class Result:
	code: int
	msg: str
	data: dict

	@classmethod
	def success(cls, data=None):
		return Result(API["SUCCESS_CODE"], 'success', to_camel(data))

	# 一般都用HttpException
	@classmethod
	def fail(cls, code: int, msg: str):
		return Result(400, msg, {})

	@classmethod
	def page(cls, lst: list):
		return Result.success({
			"total": len(lst),
			"records": lst
		})
