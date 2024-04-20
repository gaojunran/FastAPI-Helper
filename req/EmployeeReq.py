from dataclasses import dataclass

from pydantic import BaseModel, Field


class EmployeeLoginReq(BaseModel):
	"""EmployeeLoginDTO，员工登录时传递的数据模型"""
	"""密码"""
	password: str
	"""用户名"""
	username: str


class EmployeeCommon(BaseModel):
	"""EmployeeDTO"""
	id: int
	idNumber: str
	name: str = Field(default="", max_length=10)
	phone: str
	sex: str
	username: str
