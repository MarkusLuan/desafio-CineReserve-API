from abc import ABC
from typing import TypeVar, Generic

from ..models.abstract_model import AbstractModel
from ..models.filters import PaginacaoFilter
from .. import app_singleton

T_MODEL = TypeVar("T_MODEL", bound=AbstractModel)

class AbstractRepository (ABC, Generic[T_MODEL]):
    model = AbstractModel
    dto_filters = []
    joins = []
    is_paginate = True
    is_can_get = True
    is_can_insert = False

    def __init__(self):
        if self.is_paginate:
            self.dto_filters.append(PaginacaoFilter)

    def check_ja_existente(self, entity: T_MODEL):
        ...

    def get(self, *args, **kwargs):
        if not self.is_can_get:
            raise NotImplementedError()

        session = app_singleton.db.session
        query = session.query(self.model)

        for join in self.joins:
            query = query.join(join)

        for dto_filter_cls in self.dto_filters:
            dto_filter = dto_filter_cls(**kwargs)
            query = dto_filter.make_filter(query)
        
        return query.all()
    
    def insert(self, entity: T_MODEL) -> T_MODEL:
        if not self.is_can_insert:
            raise NotImplementedError()

        self.check_ja_existente(entity)
        
        session = app_singleton.db.session
        session.add(entity)
        session.commit()
        return entity