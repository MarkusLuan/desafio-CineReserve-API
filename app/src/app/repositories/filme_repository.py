from .abstract_repository import AbstractRepository
from ..models.filters import FilmeFilter
from ..models import Filme

class FilmeRepository (AbstractRepository):
    model = Filme
    dto_filters = [ FilmeFilter ]