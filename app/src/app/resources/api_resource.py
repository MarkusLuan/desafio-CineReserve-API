from flask import Blueprint
import flask_restful as Rest

from .filme_resource import FilmeResource
from .sessao_resource import SessaoResource
from .usuario_resource import UsuarioResource

resources = Blueprint("api", __name__, url_prefix="/api")

api = Rest.Api(resources)
api.add_resource(FilmeResource, "/filmes/")
api.add_resource(SessaoResource, "/sessoes/")
api.add_resource(UsuarioResource, "/usuarios/")