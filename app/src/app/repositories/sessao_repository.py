import uuid

from .abstract_repository import AbstractRepository
from ..models import Sessao, Filme
from ..models.filters import SessaoFilter
from .. import app_singleton

class SessaoRepository (AbstractRepository [Sessao]):
    model = Sessao
    dto_filters = [ SessaoFilter ]
    joins = [ Filme ]

    def get_by_uuid(self, uuid_sessao: uuid.UUID):
        session = app_singleton.db.session
        query = session.query(Sessao)
        query = query.filter(Sessao.uuid == str(uuid_sessao))

        return query.first()