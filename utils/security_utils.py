import datetime

import jwt
import hashlib

from settings import JWT


def get_md5_hexdigest(password: str) -> str:
	# 将密码字符串编码为字节
	password_bytes = password.encode('utf-8')

	# 创建MD5哈希对象
	md5_hash = hashlib.md5()

	# 对密码字节进行哈希计算
	md5_hash.update(password_bytes)

	# 获取16进制的哈希字符串
	md5_hexdigest = md5_hash.hexdigest()

	return md5_hexdigest


def config_jwt(claims: dict, algorithm='HS256'):
	# 配置JWT
	ADMIN_SECRET_KEY = JWT["ADMIN_SECRET_KEY"]
	ADMIN_TTL = JWT["ADMIN_TTL"]

	claims["exp"] = datetime.datetime.utcnow() + datetime.timedelta(seconds=ADMIN_TTL)

	# 生成JWT令牌
	token = jwt.encode(
		claims,  # 令牌内容
		ADMIN_SECRET_KEY,  # 密钥
		algorithm=algorithm  # 加密算法
	)
	return token