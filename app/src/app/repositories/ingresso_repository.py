import re
import uuid
import typing

from sqlalchemy import and_

from .abstract_repository import AbstractRepository
from .usuario_repository import UsuarioRepository
from ..models import Ingresso, Sessao, Usuario
from ..models.enums import StatusAssentoEnum
from .. import app_singleton

class IngressoRepository (AbstractRepository [Ingresso]):
    usuario_repository = UsuarioRepository()
    model = Ingresso
    dto_filters = [  ]
    is_can_insert = True
    is_paginate = True

    def organizar_assentos (self, lista_assentos: typing.List[int]):
        res = []
        if not lista_assentos:
            return res
        
        lista_assentos = sorted(lista_assentos)
        inicio_sequencia = lista_assentos[0]
        anterior = lista_assentos[0]

        for atual in lista_assentos[1:]:
            if atual == anterior + 1:
                anterior = atual
                continue
            
            if inicio_sequencia == anterior:
                res.append(str(inicio_sequencia))
            else:
                res.append(f"{inicio_sequencia}-{anterior}")
            inicio_sequencia = atual
            anterior = atual
        
        if inicio_sequencia == anterior:
            res.append(str(inicio_sequencia))
        else:
            res.append(f"{inicio_sequencia}-{anterior}")
        
        return res
    
    def get_assentos_pre_reservados(self, uuid_sessao: uuid.UUID):
        res = []
        keys = app_singleton.redis_cli.keys(f"s:{uuid_sessao}:a:*")

        if not keys:
            return res

        for k in keys:
            pattern = re.compile(r"a:([0-9]+)")
            m = pattern.search(k.decode())

            indice_assento = int(m.group(1))
            res.append(indice_assento)
        
        return res

    
    def key_reserva (self, uuid_sessao: uuid.UUID, assento: int):
        return f"s:{uuid_sessao}:a:{assento}"

    def get_meus_ingressos(self, usuario: Usuario):
        session = app_singleton.db.session
        query = session.query(Ingresso)
        query = query.join(Usuario)
        query = query.filter(Usuario.uuid == usuario.uuid)
        return query.all()
    
    def get_ingressos_comprados(self, uuid_sessao: uuid.UUID):
        session = app_singleton.db.session
        query = session.query(Ingresso)
        query = query.join(Sessao)
        query = query.filter(and_(
            Sessao.uuid == str(uuid_sessao),
            Ingresso.status_assento == StatusAssentoEnum.COMPRADO
        ))
        
        return query.all()

    def get_assentos(self, uuid_sessao: uuid.UUID):
        res = { k.name: [] for k in list(StatusAssentoEnum)}
        ingressos_comprados = self.get_ingressos_comprados(uuid_sessao)

        session = app_singleton.db.session
        query = session.query(Sessao)
        query = query.filter(Sessao.uuid == str(uuid_sessao))

        sessao_filme = query.first()
        if not sessao_filme:
            raise Exception("Sessão não encontrada!")
        
        quant_assentos_max = sessao_filme.quant_assentos
        
        assentos_reservados = self.get_assentos_pre_reservados(uuid_sessao)
        assentos_comprados = [ ic.assento for ic in ingressos_comprados ]
        assentos_disponiveis = [ a for a in range(1, quant_assentos_max) if a not in assentos_comprados ]

        res[StatusAssentoEnum.RESERVADO.name] = self.organizar_assentos(assentos_reservados)
        res[StatusAssentoEnum.COMPRADO.name] = self.organizar_assentos(assentos_comprados)
        res[StatusAssentoEnum.DISPONIVEL.name] = self.organizar_assentos(assentos_disponiveis)
        return res
    
    def is_assento_disponivel (self, uuid_sessao: uuid.UUID, indice_assento: int):
        if indice_assento < 1:
            return False
        
        reserva = app_singleton.redis_cli.get(self.key_reserva(uuid_sessao, indice_assento))
        if reserva:
            if str(reserva.decode()) != str(self.usuario_repository.get_logged_user().uuid):
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