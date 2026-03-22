import datetime
import uuid

from sqlalchemy.orm import Query
from sqlalchemy import and_

from .abstract_filter import AbstractFilter

from ..sessao import Sessao
from ..filme import Filme
from .dto_filter import DTOFilter

class SessaoFilter (AbstractFilter):
    def __init__(self, *args, **kwargs) -> None:
        self.uuid_filme = DTOFilter("uuid_filme", uuid.UUID, is_obrigatorio=True)
        self.dt_inicial = DTOFilter("dt_inicial", datetime.datetime, None)
        self.dt_final = DTOFilter("dt_final", datetime.datetime, None)
        
        super().__init__(*args, **kwargs)
    
    def make_filter(self, query: Query) -> Query:
        query = query.filter(Filme.uuid == str(self.uuid_filme.valor))

        if self.dt_inicial and self.dt_final:
            query = query.filter(and_(
                    Sessao.dt_sessao >= self.dt_inicial.valor,
                     Sessao.dt_sessao <= self.dt_final.valor
                ))
        else:
            if self.dt_inicial:
                query = query.filter(Sessao.dt_sessao >= self.dt_inicial.valor)
            elif self.dt_final:
                query = query.filter(Sessao.dt_sessao <= self.dt_final.valor)
        return query