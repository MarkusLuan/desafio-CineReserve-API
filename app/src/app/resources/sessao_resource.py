from .abstract_resource import AbstractResource
from ..repositories import SessaoRepository

class SessaoResource (AbstractResource):
    repository = SessaoRepository()
    methods = ["GET"]