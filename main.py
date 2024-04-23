from fastapi import FastAPI

from apis.employee_api import router as employee_router
from apis.dish_api import router as dish_router
from tortoise.contrib.fastapi import register_tortoise

from settings import TORTOISE_ORM

app = FastAPI()
app.include_router(employee_router, tags=[])
app.include_router(dish_router)

register_tortoise(
	app=app, config=TORTOISE_ORM,
	generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
	add_exception_handlers=True  # 生产环境不要开，会泄露调试信息
)

@app.get("/")
async def root():
	return {"message": "Hello World"}
