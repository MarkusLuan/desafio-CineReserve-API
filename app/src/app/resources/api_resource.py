from flask import Blueprint
import flask_restful as Rest

from .filme_resource import FilmeResource
from .sessao_resource import SessaoResource
from .usuario_resource import UsuarioResource
from .ingresso_resource import IngressoResource
from .assento_resource import resources as AssentoResource
from .auth_resource import resources as AuthResource

resources = Blueprint("api", __name__, url_prefix="/api")
resources.register_blueprint(AssentoResource)
resources.register_blueprint(AuthResource)

api = Rest.Api(resources)
api.add_resource(FilmeResource, "/filmes/")
api.add_resource(SessaoResource, "/filmes/<uuid:uuid_filme>/sessoes/")
api.add_resource(UsuarioResource, "/usuarios/")
api.add_resource(IngressoResource, "/meus_ingressos/")
