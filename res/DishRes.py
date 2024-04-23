from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel

@dataclass
class DishFlavor:
	"""DishFlavor"""
	dishId: int | None = None
	id: int | None = None
	name: str | None = None
	value: str | None = None

@dataclass
class DishCommonRes:
	"""DishVO"""
	categoryId: int | None = None
	categoryName: str | None = None
	description: str | None = None
	flavors: list[DishFlavor] | None = None
	id: int | None = None
	image: str | None = None
	name: str | None = None
	price: float | None = None
	status: int | None = None
	updateTime: datetime | None = None
