from fastapi import APIRouter

from models.models import Dish, Flavor
from req.DishReq import DishCommonReq
from res.DishRes import DishCommonRes
from static.Result import Result
from utils.api_utils import copyattr, update_by_id

router = APIRouter(prefix="/admin/dish")

DISH_SKIP = ("flavors",)


@router.get("/{id}")
async def get_by_id(id: int):
	dish = await Dish.get(id=id)
	dishCommonRes = copyattr(dish, DishCommonRes())
	flavors: list[dict] = await dish.flavors.all().values("id", "name", "value")
	for i in flavors:
		i["dish_id"] = id
	dishCommonRes.flavors = flavors
	return Result.success(dishCommonRes)


@router.post("/")
async def save(req: DishCommonReq):
	dish: Dish = copyattr(req, Dish(), skip=DISH_SKIP)
	dish.create_user = 1
	dish.update_user = 1
	await dish.save()
	for flavor in req.flavors:
		flavor = copyattr(flavor, Flavor())
		flavor.create_user = 1
		flavor.update_user = 1
		await flavor.save()
		await dish.flavors.add(flavor)  # 关联记录
	return Result.success()


@router.put("/")
async def update(req: DishCommonReq):
	dish: Dish = copyattr(req, Dish(), skip=DISH_SKIP)
	await update_by_id(dish)
	dish.create_user = 1
	dish.update_user = 1
	await dish.save()
	await dish.flavors.clear()
	for flavor in req.flavors:
		flavor = copyattr(flavor, Flavor())
		flavor.create_user = 1
		flavor.update_user = 1
		await flavor.save()
		await dish.flavors.add(flavor)
	return Result.success()


@router.delete("/")
async def deleteBatch(ids: str):
	id_list = ids.split(",")
	for id in id_list:
		dish = await Dish.get(id=id)
		await dish.flavors.clear()
		await dish.delete()
	return Result.success()
