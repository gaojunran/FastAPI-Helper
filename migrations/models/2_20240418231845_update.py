from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `category` MODIFY COLUMN `create_user` INT NOT NULL;
        ALTER TABLE `category` MODIFY COLUMN `update_user` INT NOT NULL;
        ALTER TABLE `dish` MODIFY COLUMN `create_user` INT NOT NULL;
        ALTER TABLE `dish` MODIFY COLUMN `update_user` INT NOT NULL;
        ALTER TABLE `employee` MODIFY COLUMN `create_user` INT NOT NULL;
        ALTER TABLE `employee` MODIFY COLUMN `update_user` INT NOT NULL;
        ALTER TABLE `generalmodel` MODIFY COLUMN `update_user` INT NOT NULL;
        ALTER TABLE `generalmodel` MODIFY COLUMN `create_user` INT NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `dish` MODIFY COLUMN `create_user` VARCHAR(50) NOT NULL;
        ALTER TABLE `dish` MODIFY COLUMN `update_user` VARCHAR(50) NOT NULL;
        ALTER TABLE `category` MODIFY COLUMN `create_user` VARCHAR(50) NOT NULL;
        ALTER TABLE `category` MODIFY COLUMN `update_user` VARCHAR(50) NOT NULL;
        ALTER TABLE `employee` MODIFY COLUMN `create_user` VARCHAR(50) NOT NULL;
        ALTER TABLE `employee` MODIFY COLUMN `update_user` VARCHAR(50) NOT NULL;
        ALTER TABLE `generalmodel` MODIFY COLUMN `update_user` VARCHAR(50) NOT NULL;
        ALTER TABLE `generalmodel` MODIFY COLUMN `create_user` VARCHAR(50) NOT NULL;"""
