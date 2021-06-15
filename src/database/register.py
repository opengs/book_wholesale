import logging, traceback

from fastapi import FastAPI
from tortoise import Tortoise, fields

from .fill import fill_with_test_data

def register_tortoise(
        app: FastAPI,
        db_url: str,
        generate_schemas: bool = False,
    ) -> None:
    '''Registers tortoise orm'''

    async def init_orm():
        try:
            await Tortoise.init(
                db_url=db_url,
                modules={
                    "models": [
                        "src.database.models.book",
                        "src.database.models.order",
                        "src.database.models.orderDetails",
                        "src.database.models.systemUser",
                        "src.database.models.user",
                    ]
                }
            )
            logging.info('Tortoise-ORM started, %s, %s', Tortoise._connections, Tortoise.apps)
            if generate_schemas:
                logging.info('Tortoise-ORM generating schema.')
                await Tortoise.generate_schemas()
                await fill_with_test_data()
        except Exception as e:
                logging.error(e)
                traceback.print_exc()

    async def close_orm():
        try:
            logging.info('Tortoise-ORM shutting down.')
            await Tortoise.close_connections()
        except Exception as e:
                logging.error(e)
                traceback.print_exc()


    app.add_event_handler("startup", init_orm)
    app.add_event_handler("shutdown", close_orm)