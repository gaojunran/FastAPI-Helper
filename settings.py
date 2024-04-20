TORTOISE_ORM = {
	'connections': {
		'default': {
			# 'engine': 'tortoise.backends.asyncpg',  PostgreSQL
			'engine': 'tortoise.backends.mysql',  # MySQL or Mariadb
			'credentials': {
				'host': '127.0.0.1',
				'port': '3306',
				'user': 'root',
				'password': '123456',
				'database': 'sky_fastapi',
				'minsize': 1,
				'maxsize': 5,
				'charset': 'utf8mb4',
				"echo": True
			}
		},
	},
	'apps': {
		'models': {
			'models': ['models.models', "aerich.models"],  # 前面这个是自定义的模型类路径，aerich这个也可以不加
			'default_connection': 'default',

		}
	},
	'use_tz': False,
	'timezone': 'Asia/Shanghai'
}

JWT = {
	"ADMIN_SECRET_KEY": "itcast",  # 替换为你的JWT密钥
	"ADMIN_TTL": 7200000  # 令牌有效时间，单位秒
}

API = {
	"SUCCESS_CODE": 1
}
