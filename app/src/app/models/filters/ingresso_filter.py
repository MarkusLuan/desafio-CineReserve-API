import datetime
import uuid

from sqlalchemy.orm import Query
from sqlalchemy import and_

from .abstract_filter import AbstractFilter

from ..ingresso import Ingresso
from ..usuario import Usuario
from .dto_filter import DTOFilter

class IngressoFilter (AbstractFilter):
    def __init__(self, *args, **kwargs) -> None:
        self.uuid_usuario = DTOFilter("uuid_usuario", uuid.UUID, is_obrigatorio=True)
        self.dt_inicial = DTOFilter("dt_inicial", datetime.datetime, None)
        self.dt_final = DTOFilter("dt_final", datetime.datetime, None)

        super().__init__(*args, **kwargs)

    def make_filter(self, query: Query) -> Query:
        query = query.filter(Usuario.uuid == str(self.uuid_usuario.valor))

        if self.dt_inicial and self.dt_final:
            query = query.filter(and_(
                    Ingresso.dt_reserva >= self.dt_inicial.valor,
                     Ingresso.dt_reserva <= self.dt_final.valor
                ))
        else:
            if self.dt_inicial:
                query = query.filter(Ingresso.dt_reserva >= self.dt_inicial.valor)
            elif self.dt_final:
                query = query.filter(Ingresso.dt_reserva <= self.dt_final.valor)
        return query