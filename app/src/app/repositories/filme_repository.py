from .abstract_repository import AbstractRepository
from ..models.filters import FilmeFilter
from ..models import Filme

class FilmeRepository (AbstractRepository [Filme]):
    model = Filme
    dto_filters = [ FilmeFilter ]