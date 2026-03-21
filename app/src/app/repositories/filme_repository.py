from .abstract_repository import AbstractRepository
from ..models import Filme

class FilmeRepository (AbstractRepository):
    model = Filme