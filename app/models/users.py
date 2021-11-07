import uuid

from tortoise.fields import (
    IntField, UUIDField, CharField,
    BooleanField, CharEnumField
)
from tortoise.models import Model

from app.models.mixins import ObjChangesDatetimeMixin
from app.models.enums import UserRoleEnum


class UserModel(Model, ObjChangesDatetimeMixin):
    '''Model to describe users table in DB'''
    id = IntField(pk=True)
    public_id = UUIDField(unique=True, default=uuid.uuid4)
    full_name = CharField(max_length=255)
    email = CharField(unique=True, max_length=120)
    password = CharField(max_length=128)
    is_active = BooleanField(default=True)
    position = CharField(max_length=255)
    role = CharEnumField(
        UserRoleEnum, description='User roles'
    )


    class Meta:
        table = 'users'
