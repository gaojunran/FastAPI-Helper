# FastAPI单体后端项目模板

施工中，目前包含：

1. 业务CRUD代码模板（单表、多表）
2. 下划线-驼峰转换工具类
3. 分页查询工具、按id查询工具
4. JWT生成工具类（校验还没做）

## 教程

1. 初始化FastAPI项目、安装Tortoise ORM、数据迁移工具等
    ```bash
    pip install tortoise-orm
    pip install aerich
    pip install aiomysql
    pip install PyJWT
    pip install cryptography
    ```

2. 项目结构搭建

    ```
    - apis
    - entity
    - req
    - res
    - static
    ```

3. 搭建路由`apis`。在子路由中新建`router = APIRouter(prefix="/admin")`，再在`main.py`中加入这个路由：

    ```python
    from apis.employee_api import router as employee_router
    from apis.dish_api import router as dish_router
    
    app = FastAPI()
    app.include_router(employee_router)
    app.include_router(dish_router)
    ```

4. 定义工具，将属性的命名风格在下划线和小驼峰之间互换。

    ```python
    def underscore_to_camelcase(s):
        parts = s.split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])
    
    def to_camel(d):  # 暂不支持BaseModel套BaseModel的情况:
        if isinstance(d, BaseModel):
            return to_camel(d.dict())
        elif isinstance(d, dict):
            return {underscore_to_camelcase(k): to_camel(v) for k, v in d.items()}
        elif isinstance(d, list):
            return [to_camel(item) for item in d]
        else:
            return d
    
    def camelcase_to_underscore(s):
        s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
    
    def to_under(d):
        if isinstance(d, BaseModel):
            return to_under(d.dict())
        elif isinstance(d, dict):
            return {camelcase_to_underscore(k): to_under(v) for k, v in d.items()}
        elif isinstance(d, list):
            return [to_under(item) for item in d]
        else:
            return d
    ```

5. 定义工具，模拟`BeanUtils.copyProperties()`复制两个不同类对象的公有属性。

    ```python
    def copyattr(source, target, converter=camelcase_to_underscore):
        # 遍历源对象的属性
        for attr in dir(source):
            # 如果属性是方法或私有属性，则跳过
            if attr.startswith('__') or attr.startswith('_') or callable(getattr(source, attr)):
                continue
            # 如果目标对象也有这个属性，则复制它
            new_attr = converter(attr) if converter else attr
            if hasattr(target, new_attr):
                setattr(target, new_attr, getattr(source, attr))
        return target
    ```

6. 定义`Result`响应模板类。

    ```python
    @dataclass
    class Result:
        code: int
        msg: str
        data: dict
    
        @classmethod
        def success(cls, data: dict | list):
            return Result(200, 'success', to_camel(data))
    
        @classmethod
        def fail(cls, msg: str):
            return Result(400, msg, {})
    ```

7. 定义模型类。
    1. 可以定义一个通用模型类：

        ```python
        from tortoise import fields
        from tortoise.models import Model
        
        class GeneralModel(Model):
            create_time = fields.DatetimeField(auto_now_add=True)
            update_time = fields.DatetimeField(auto_now=True)
            create_user = fields.IntField()
            update_user = fields.IntField()
        ```

    2. 编写数据库对应模型类：

       一对多关系：`ForeignKeyField`要把外键定义在“多”的数据库表中；

       多对多关系：

       [深度理解Django模型关联中的两个重要参数 :related_name和related_query_name-CSDN博客](https://blog.csdn.net/coolzpf/article/details/132844054)

8. 请求、响应、模型类

   受`copyattr`工具类的影响，对请求/响应模型类的类型作以下规定：

    1. 注意请求模型类中可以设定校验条件，使用`Pydantic`，除非业务要求，一般是非空的；
    2. 注意响应模型类中可以使用`dataclass`，但必须将所有字段设为可空并提供`None`默认值，以调用空参构造。
    3. 表实体模型类中应当包含表中的所有字段（以数据库实际呈现的为准）。
9. 数据库迁移
    1. 基本配置

        ```python
        # main.py
        register_tortoise(
        	app=app, config=TORTOISE_ORM,
        	generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
        	add_exception_handlers=True  # 生产环境不要开，会泄露调试信息
        )
        
        # settings.py
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
        			'models': ['models.models', "aerich.models"], # 前面这个是自定义的模型类路径，aerich这个也可以不加
        			'default_connection': 'default',
        
        		}
        	},
        	'use_tz': False,
        	'timezone': 'Asia/Shanghai'
        }
        ```

    2. 运行项目，初始化建表
    3. 初始化配置（只使用一次）：`aerich init -t settings.TORTOISE_ORM`

       生成`pyproject.toml`，保存配置文件路径；

       生成文件夹`migrations`，存放迁移文件。

    4. 初始化数据库（一般只使用一次）：`aerich init-db`
    5. 执行迁移：`aerich migrate`; `aerich upgrade`
10. CRUD接口
    1. 封装工具函数：按id更新`update_by_id()`

        ```python
        def _get_update_entries(obj: GeneralModel):
            return {k: v for k, v in dict(obj).items() if k != "id" and v is not None and v != ""}
        
        async def update_by_id(obj: GeneralModel):
            cls = obj.__class__
            await cls.filter(id=obj.id).update(**_get_update_entries(obj))
        ```

    2. ORM的操作必须是`异步`的；
    3. 单表CRUD
        1. 查询：查询所有`all()`；查询多个`filter()`；查询一个`get()`；返回特定字段的字典`.values()`。
        2. 按字段创建/更新：`create`、`update`
        3. 按对象创建/更新：`对象.save`
        4. 删除：`delete`
    4. 多表CRUD
        1. 查询

           通过正查名和反查名，获取到从表：

           “对一”关系的查询可以直接获取到`.values()`或具体的字段名；“对多”关系的查询则需要先调用`all`、`get`或`filter`；

           如果要使用`filter`方法，传入的关键字参数应为`正反查表名__字段名__条件`。

        2. 添加

           分别给两个表单独添加后，通过正查名和反查名的`.add()`方法添加多对多的关系记录，方法传入从表的模型类对象。

           注意，添加前必须要调用两个表的`.save()`方法。

        3. 更新

           确认关联关系没变时：正常更新即可。

           关联关系可能发生改变时：给主表更新后，通过正反查名的`.clear()`方法清空关联关系，再通过`.add()`添加关联关系。

        4. 删除

           调用正反查名的`.clear()`方法清空关联关系，或调用正反查名的`.delete()`方法清除关联关系。