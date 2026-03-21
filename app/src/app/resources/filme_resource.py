from .abstract_resource import AbstractResource
from ..repositories import FilmeRepository

class FilmeResource (AbstractResource):
    repository = FilmeRepository()
    methods = ["GET"]