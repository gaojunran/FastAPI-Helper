from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `category` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `create_user` INT NOT NULL,
    `update_user` INT NOT NULL,
    `type` INT NOT NULL  COMMENT '类型   1 菜品分类 2 套餐分类',
    `name` VARCHAR(50) NOT NULL  COMMENT '分类名称',
    `sort` INT NOT NULL  COMMENT '顺序',
    `status` INT NOT NULL  COMMENT '分类状态 0:禁用，1:启用'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `dish` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `create_user` INT NOT NULL,
    `update_user` INT NOT NULL,
    `name` VARCHAR(50) NOT NULL  COMMENT '菜品名称',
    `price` DOUBLE NOT NULL  COMMENT '菜品价格',
    `image` VARCHAR(255) NOT NULL  COMMENT '图片',
    `description` VARCHAR(255) NOT NULL  COMMENT '描述信息',
    `status` INT NOT NULL  COMMENT '0 停售; 1 起售',
    `category_id` INT NOT NULL COMMENT '菜品分类id',
    CONSTRAINT `fk_dish_category_eb96f2fb` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `employee` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `create_user` INT NOT NULL,
    `update_user` INT NOT NULL,
    `name` VARCHAR(50) NOT NULL  COMMENT '姓名',
    `username` VARCHAR(50) NOT NULL  COMMENT '用户名',
    `password` VARCHAR(50) NOT NULL  COMMENT '密码',
    `phone` VARCHAR(50) NOT NULL  COMMENT '手机号',
    `sex` VARCHAR(50) NOT NULL  COMMENT '性别',
    `id_number` VARCHAR(50) NOT NULL  COMMENT '身份证号',
    `status` INT NOT NULL  COMMENT '状态 0:禁用，1:启用'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `flavor` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `create_user` INT NOT NULL,
    `update_user` INT NOT NULL,
    `name` VARCHAR(32) NOT NULL  COMMENT '口味名称',
    `value` VARCHAR(255) NOT NULL  COMMENT '口味值'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `generalmodel` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `create_user` INT NOT NULL,
    `update_user` INT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `setmeal` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `create_user` INT NOT NULL,
    `update_user` INT NOT NULL,
    `category` INT NOT NULL  COMMENT '菜品分类id',
    `name` VARCHAR(50) NOT NULL  COMMENT '套餐名称',
    `price` DOUBLE NOT NULL  COMMENT '套餐价格',
    `status` INT NOT NULL  COMMENT '售卖状态 0:停售 1:起售',
    `description` VARCHAR(255) NOT NULL  COMMENT '描述信息',
    `image` VARCHAR(255) NOT NULL  COMMENT '图片'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `dish_flavor` (
    `dish_id` INT NOT NULL,
    `flavor_id` INT NOT NULL,
    FOREIGN KEY (`dish_id`) REFERENCES `dish` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`flavor_id`) REFERENCES `flavor` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='口味';
CREATE TABLE IF NOT EXISTS `setmeal_dish` (
    `setmeal_id` INT NOT NULL,
    `dish_id` INT NOT NULL,
    FOREIGN KEY (`setmeal_id`) REFERENCES `setmeal` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`dish_id`) REFERENCES `dish` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='菜品';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
