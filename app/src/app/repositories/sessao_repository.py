from .abstract_repository import AbstractRepository
from ..models import Sessao, Filme
from ..models.filters import SessaoFilter

class SessaoRepository (AbstractRepository):
    model = Sessao
    dto_filters = [ SessaoFilter ]
    joins = [ Filme ]