from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel

@dataclass
class EmployeeLoginRes:
    """EmployeeLoginVO，员工登录返回的数据格式"""
    """主键值"""
    id: Optional[int] = None
    """姓名"""
    name: Optional[str] = None
    """jwt令牌"""
    token: Optional[str] = None
    """用户名"""
    username: Optional[str] = None
