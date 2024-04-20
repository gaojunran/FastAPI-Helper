from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Employee:
    """Employee"""
    """主键"""
    id: int
    """身份证号"""
    id_number: str
    """姓名"""
    name: str
    """密码"""
    password: str
    """手机号"""
    phone: str
    """性别"""
    sex: str
    """状态 0:禁用，1:启用"""
    status: int
    """用户名"""
    username: str
    """创建时间"""
    create_time: Optional[datetime] = None
    """创建人"""
    create_user: Optional[int] = None
    """更新时间"""
    update_time: Optional[datetime] = None
    """修改人"""
    update_user: Optional[int] = None