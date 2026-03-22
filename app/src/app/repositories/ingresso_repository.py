import uuid

from sqlalchemy import and_

from .abstract_repository import AbstractRepository
from ..models import Ingresso, Sessao
from ..models.enums import StatusAssentoEnum
from .. import app_singleton

class IngressoRepository (AbstractRepository [Ingresso]):
    model = Ingresso
    dto_filters = [  ]
    is_can_insert = True
    is_paginate = True

    def get_assentos(self, uuid_sessao: uuid.UUID):
        res = { k.name: [] for k in list(StatusAssentoEnum)}

        session = app_singleton.db.session
        query = session.query(Sessao)
        query = query.filter(Sessao.uuid == str(uuid_sessao))

        sessao_filme = query.first()
        if not sessao_filme:
            raise Exception("Sessão não encontrada!")
        
        quant_assentos_max = sessao_filme.quant_assentos
        # TODO: Juntar com os ingressos para ver quais os assentos estão reservados

        res[StatusAssentoEnum.DISPONIVEL.name] = [f"1-{quant_assentos_max}"]
        return res
    
    def is_assento_disponivel (self, uuid_sessao: uuid.UUID, indice_assento: int):
        if indice_assento < 1:
            return False
        
        session = app_singleton.db.session
        query = session.query(Ingresso)
        query = query.join(Sessao)
        query = query.filter(and_(
            Sessao.uuid == str(uuid_sessao),
            Ingresso.assento == indice_assento
        ))

        assento = query.first()
        return not assento