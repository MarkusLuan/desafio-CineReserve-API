from .abstract_repository import AbstractRepository
from ..models import Sessao, Filme
from ..models.filters import SessaoFilter

class SessaoRepository (AbstractRepository [Sessao]):
    model = Sessao
    dto_filters = [ SessaoFilter ]
    joins = [ Filme ]