from tortoise import fields
from tortoise.models import Model
from models.GeneralModel import GeneralModel

"""
{
    "properties": {
        "id": {
            "description": "主键",
            "type": "integer",
            "minimum": 1,
            "maximum": 2147483647
        },
        "name": {
            "description": "姓名",
            "type": "string",
            "maxLength": 32
        },
        "username": {
            "description": "用户名",
            "type": "string",
            "maxLength": 32
        },
        "password": {
            "description": "密码",
            "type": "string",
            "maxLength": 64
        },
        "phone": {
            "description": "手机号",
            "type": "string",
            "maxLength": 11
        },
        "sex": {
            "description": "性别",
            "type": "string",
            "maxLength": 2
        },
        "id_number": {
            "description": "身份证号",
            "type": "string",
            "maxLength": 18
        },
        "status": {
            "description": "状态 0:禁用，1:启用",
            "default": "1",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        },
        "create_time": {
            "description": "创建时间",
            "type": "string",
            "format": "date-time"
        },
        "update_time": {
            "description": "更新时间",
            "type": "string",
            "format": "date-time"
        },
        "create_user": {
            "description": "创建人",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        },
        "update_user": {
            "description": "修改人",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        }
    },
    "type": "object",
    "required": [
        "id",
        "name",
        "username",
        "password",
        "phone",
        "sex",
        "id_number",
        "status"
    ],
    "x-apifox-orders": [
        "id",
        "name",
        "username",
        "password",
        "phone",
        "sex",
        "id_number",
        "status",
        "create_time",
        "update_time",
        "create_user",
        "update_user"
    ]
}
"""


class Employee(GeneralModel):
	id = fields.IntField(pk=True)
	name = fields.CharField(max_length=50, description="姓名")
	username = fields.CharField(max_length=50, description="用户名")
	password = fields.CharField(max_length=50, description="密码")
	phone = fields.CharField(max_length=50, description="手机号")
	sex = fields.CharField(max_length=50, description="性别")
	id_number = fields.CharField(max_length=50, description="身份证号")
	status = fields.IntField(description="状态 0:禁用，1:启用")


"""
{
    "properties": {
        "id": {
            "description": "主键",
            "type": "integer",
            "minimum": 1,
            "maximum": 2147483647
        },
        "name": {
            "description": "菜品名称",
            "type": "string",
            "maxLength": 32
        },
        "category_id": {
            "description": "菜品分类id",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        },
        "price": {
            "description": "菜品价格",
            "type": "number"
        },
        "image": {
            "description": "图片",
            "type": "string",
            "maxLength": 255
        },
        "description": {
            "description": "描述信息",
            "type": "string",
            "maxLength": 255
        },
        "status": {
            "description": "0 停售 1 起售",
            "default": "1",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        },
        "create_time": {
            "description": "创建时间",
            "type": "string",
            "format": "date-time"
        },
        "update_time": {
            "description": "更新时间",
            "type": "string",
            "format": "date-time"
        },
        "create_user": {
            "description": "创建人",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        },
        "update_user": {
            "description": "修改人",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        }
    },
    "type": "object",
    "required": [
        "id",
        "name",
        "category_id"
    ],
    "x-apifox-orders": [
        "id",
        "name",
        "category_id",
        "price",
        "image",
        "description",
        "status",
        "create_time",
        "update_time",
        "create_user",
        "update_user"
    ]
}
"""


class Dish(GeneralModel):
	id = fields.IntField(pk=True)
	name = fields.CharField(max_length=50, description="菜品名称")
	# category_id = fields.IntField(description="菜品分类id")
	category = fields.ForeignKeyField("models.Category", related_name="dishes", description="菜品分类id")
	price = fields.FloatField(description="菜品价格")
	image = fields.CharField(max_length=255, description="图片")
	description = fields.CharField(max_length=255, description="描述信息")
	status = fields.IntField(description="0 停售; 1 起售")


"""{
    "properties": {
        "id": {
            "description": "主键",
            "type": "integer",
            "minimum": 1,
            "maximum": 2147483647
        },
        "type": {
            "description": "类型   1 菜品分类 2 套餐分类",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        },
        "name": {
            "description": "分类名称",
            "type": "string",
            "maxLength": 32
        },
        "sort": {
            "description": "顺序",
            "default": "0",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        },
        "status": {
            "description": "分类状态 0:禁用，1:启用",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        },
        "create_time": {
            "description": "创建时间",
            "type": "string",
            "format": "date-time"
        },
        "update_time": {
            "description": "更新时间",
            "type": "string",
            "format": "date-time"
        },
        "create_user": {
            "description": "创建人",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        },
        "update_user": {
            "description": "修改人",
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        }
    },
    "type": "object",
    "required": [
        "id",
        "name",
        "sort"
    ],
    "x-apifox-orders": [
        "id",
        "type",
        "name",
        "sort",
        "status",
        "create_time",
        "update_time",
        "create_user",
        "update_user"
    ]
}"""


class Category(GeneralModel):
	id = fields.IntField(pk=True)
	type = fields.IntField(description="类型   1 菜品分类 2 套餐分类")
	name = fields.CharField(max_length=50, description="分类名称")
	sort = fields.IntField(description="顺序")
	status = fields.IntField(description="分类状态 0:禁用，1:启用")


if __name__ == '__main__':
	em = Employee(id=1)
	print(dict(em))
