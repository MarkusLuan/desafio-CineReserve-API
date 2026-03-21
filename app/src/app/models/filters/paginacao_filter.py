from sqlalchemy.orm import Query

from .abstract_filter import AbstractFilter
from ..dto_input import DTOInput

class PaginacaoFilter (AbstractFilter):
    first_result = DTOInput("first_result", int, 0)
    max_results = DTOInput("max_results", int, 0)

    def make_filter(self, query: Query):
        query = query.offset(self.first_result.valor)
        if self.max_results.valor > 0:
            query = query.limit(self.max_results.valor)
        
        return query