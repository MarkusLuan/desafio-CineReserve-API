from flask import Blueprint

from .api_resource import resources as ApiResource

resources = Blueprint("resources", __name__)
resources.register_blueprint(ApiResource)
