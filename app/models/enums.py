from enum import Enum


class UserRoleEnum(str, Enum):
    ADMIN = 'admin'
    MANAGER = 'manager'
    EMPLOYEE = 'employee'

