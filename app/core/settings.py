from typing import Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    '''Project settings Class'''
    PROJECT_NAME: str = 'aTES auth service'
    API_V1_STR: str = '/v1'

    # DB variables
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DATABASE_URL: Optional[PostgresDsn] = None

    @validator('DATABASE_URL', pre=True)
    def assemble_db_connection(cls, value, values):
        if isinstance(value, str):
            return value

        return PostgresDsn.build(
            scheme='postgres',
            user=values.get('DB_USER'),
            password=values.get('DB_PASSWORD'),
            host=values.get('DB_HOST'),
            port=values.get('DB_PORT'),
            path=f'/{values.get("DB_NAME") or ""}',
        )


settings = Settings()
