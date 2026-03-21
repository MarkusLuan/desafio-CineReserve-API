from .abstract_repository import AbstractRepository
from ..models import Sessao

class SessaoRepository (AbstractRepository):
    model = Sessao