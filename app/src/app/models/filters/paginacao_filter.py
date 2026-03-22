from sqlalchemy.orm import Query

from .abstract_filter import AbstractFilter
from .dto_filter import DTOFilter

class PaginacaoFilter (AbstractFilter):
    def __init__(self, *args, **kwargs) -> None:
        self.first_result = DTOFilter("first_result", int, 0)
        self.max_results = DTOFilter("max_results", int, 20)

        super().__init__(*args, **kwargs)

    def make_filter(self, query: Query):
        query = query.offset(self.first_result.valor)
        if self.max_results.valor > 0:
            query = query.limit(self.max_results.valor)
        
        return query