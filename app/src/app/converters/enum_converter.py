# pylint: disable=abstract-method

from typing import TypeVar, Generic, Type

from sqlalchemy import Dialect
from sqlalchemy.types import TypeDecorator, Integer

from ..models.enums.abstract_enum import AbstractEnum

ENUM_CLASS = TypeVar("ENUM_CLASS", bound=AbstractEnum)

class EnumConverter (TypeDecorator, Generic[ENUM_CLASS]):
    impl = Integer
    cache_ok = True

    def __init__(self, enum_class: Type[ENUM_CLASS], **kwargs):
        super().__init__(**kwargs)

        self.enum_class = enum_class
        self.ordinal_map = { e.ordinal: e for e in enum_class }

    def process_bind_param(self, value: ENUM_CLASS | None, dialect: Dialect) -> int | None:
        if value:
            return value.ordinal
    
    def process_result_value(self, value: int | None, dialect: Dialect) -> ENUM_CLASS | None:
        if value:
            return self.ordinal_map[value]
