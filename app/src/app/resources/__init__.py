from flask import Blueprint

from .filme_resource import resources as FilmeResource
from .sessao_resource import resources as SessaoResource

resources = Blueprint("resources", "resources")
resources.register_blueprint(FilmeResource)
resources.register_blueprint(SessaoResource)
