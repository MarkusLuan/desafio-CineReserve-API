import datetime
import uuid

from sqlalchemy.orm import Query
from sqlalchemy import and_

from ...exceptions import ParametroObrigatorioException
from .abstract_filter import AbstractFilter

from ..sessao import Sessao
from ..filme import Filme
from ..dto_input import DTOInput

class SessaoFilter (AbstractFilter):
    uuid_filme = DTOInput("uuid_filme", uuid.UUID)
    dt_inicial = DTOInput("dt_inicial", datetime.datetime|None, None)
    dt_final = DTOInput("dt_final", datetime.datetime|None, None)
    
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