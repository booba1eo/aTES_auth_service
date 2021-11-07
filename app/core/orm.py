from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.core.settings import settings


ORM_MODELS = [
    'aerich.models', 'app.models.users',
]

TORTOISE_ORM = {
    'connections': {
        'read_connection': settings.DATABASE_URL
    },
    'apps': {
        'models': {
            'models': ORM_MODELS,
            'default_connection': 'read_connection',
        },
    },
    'use_tz': False,
    'timezone': 'UTC'
}


def init_db(app: FastAPI) -> None:
    '''Инициализировать подключение к БД'''
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=False,
    )
