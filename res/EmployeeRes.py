from typing import Optional

from pydantic import BaseModel


class EmployeeLoginRes(BaseModel):
    """EmployeeLoginVO，员工登录返回的数据格式"""
    """主键值"""
    id: Optional[int] = None
    """姓名"""
    name: Optional[str] = None
    """jwt令牌"""
    token: Optional[str] = None
    """用户名"""
    username: Optional[str] = None
