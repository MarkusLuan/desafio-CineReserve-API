from flask import Blueprint

from .filme_resource import resources as FilmeResource

resources = Blueprint("resources", "resources")
resources.register_blueprint(FilmeResource)
