from flask import Blueprint
import flask_restful as Rest

from .filme_resource import FilmeResource
from .sessao_resource import SessaoResource
from .usuario_resource import UsuarioResource
from .auth import resources as AuthResource

resources = Blueprint("api", __name__, url_prefix="/api")
resources.register_blueprint(AuthResource)

api = Rest.Api(resources)
api.add_resource(FilmeResource, "/filmes/")
api.add_resource(SessaoResource, "/sessoes/")
api.add_resource(UsuarioResource, "/usuarios/")