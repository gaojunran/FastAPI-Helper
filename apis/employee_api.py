import logging

from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist
from tortoise.queryset import QuerySetSingle

from models.models import Employee
# from entity.Employee import Employee
from req.EmployeeReq import EmployeeCommon, EmployeeLoginReq
from res.EmployeeRes import EmployeeLoginRes
from static.Result import Result
from utils.api_utils import copyattr, update_by_id, get_offset
from utils.security_utils import get_md5_hexdigest, config_jwt

router = APIRouter(prefix="/admin/employee")


@router.post("/login")
async def login(req: EmployeeLoginReq):
	logging.info("登录请求：", req)
	username, password = req.username, req.password
	try:
		employee: QuerySetSingle | Employee = await Employee.get(username=username)
	except DoesNotExist:
		raise HTTPException(404, "账号不存在！")
	# if not employee:
	# 	pass
	password = get_md5_hexdigest(password)
	if password != employee.password:
		raise HTTPException(404, "密码错误！")
	if employee.status == 0:
		raise HTTPException(404, "账号状态异常！")
	token = config_jwt({"empId": employee.id})
	result: EmployeeLoginRes = copyattr(employee, EmployeeLoginRes())
	result.token = token
	return Result.success(result)


@router.get("/page")
async def page_query(page: int = 1, pageSize: int = 10, name: str = "") -> Result:
	limit = pageSize
	offset = await get_offset(page, pageSize)
	if name:
		result = await Employee.filter(name=name).limit(limit).offset(offset).values()
	else:
		result = await Employee.all().limit(limit).offset(offset).values()
	return Result.page(result)


@router.get("/{id}", description="根据id查询员工")
async def getById(id: int) -> Result:
	em = await Employee.get(id=id).values()
	return Result.success(em)


@router.post("/")
async def save(req: EmployeeCommon) -> Result:
	em: Employee = copyattr(req, Employee())
	em.status = 1
	em.password = "e10adc3949ba59abbe56e057f20f883e"
	em.create_user = 1
	em.update_user = 1
	await em.save()
	return Result.success()


@router.put("/")
async def update(req: EmployeeCommon) -> Result:
	em: Employee = copyattr(req, Employee())
	em.update_user = 1
	await update_by_id(em)
	return Result.success()


@router.post("/status/{status}")
async def start_or_stop(status: int, id: int):
	em = Employee(id=id, status=status)
	await update_by_id(em)
	return Result.success()

