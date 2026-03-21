from abc import ABC

from ..models.abstract_model import AbstractModel
from ..models import Paginacao
from .. import app_singleton

class AbstractRepository (ABC):
    model = AbstractModel

    def get(self, *args, **kwargs):
        paginacao = Paginacao(
            first_result = int(kwargs.get("first_result", 0)),
            max_results = int(kwargs.get("max_results", 20))
        )
        
        session = app_singleton.db.session
        query = session.query(self.model)

        query = query.offset(paginacao.first_result)
        if paginacao.max_results > 0:
            query = query.limit(paginacao.max_results)
        
        return query.all()