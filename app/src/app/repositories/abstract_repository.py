from abc import ABC

from ..models.abstract_model import AbstractModel
from ..models.filters import PaginacaoFilter
from .. import app_singleton

class AbstractRepository (ABC):
    model = AbstractModel
    dto_filters = []
    joins = []
    is_paginate = True

    def __init__(self):
        if self.is_paginate:
            self.dto_filters.append(PaginacaoFilter)

    def get(self, *args, **kwargs):
        session = app_singleton.db.session
        query = session.query(self.model)

        for join in self.joins:
            query = query.join(join)

        for dto_filter_cls in self.dto_filters:
            dto_filter = dto_filter_cls(**kwargs)
            query = dto_filter.make_filter(query)
        
        return query.all()