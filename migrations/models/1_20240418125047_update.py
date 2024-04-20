from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `dish` MODIFY COLUMN `status` INT NOT NULL  COMMENT '0 停售; 1 起售';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `dish` MODIFY COLUMN `status` INT NOT NULL  COMMENT '0 停售 1 起售';"""
