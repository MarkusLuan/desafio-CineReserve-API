from abc import ABC

from ..models.abstract_model import AbstractModel
from ..models.filters import PaginacaoFilter
from .. import app_singleton

class AbstractRepository (ABC):
    model = AbstractModel
    dto_filters = [ PaginacaoFilter ]

    def get(self, *args, **kwargs):
        session = app_singleton.db.session
        query = session.query(self.model)

        for dto_filter_cls in self.dto_filters:
            dto_filter = dto_filter_cls(**kwargs)
            query = dto_filter.make_filter(query)
        
        return query.all()