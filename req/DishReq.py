from dataclasses import dataclass
from typing import Optional, List


@dataclass
class DishFlavor:
    """DishFlavor"""
    """口味名称"""
    name: str
    """口味值"""
    value: str
    """菜品id"""
    dishId: Optional[int] = None
    """口味id"""
    id: Optional[int] = None


@dataclass
class DishCommonReq:
    """DishDTO"""
    """分类id"""
    categoryId: int
    """菜品图片路径"""
    image: str
    """菜品名称"""
    name: str
    """菜品价格"""
    price: float
    """菜品描述"""
    description: Optional[str] = None
    """口味"""
    flavors: list[DishFlavor] | None = None
    """菜品id"""
    id: Optional[int] = None
    """菜品状态：1为起售，0为停售"""
    status: Optional[int] = None