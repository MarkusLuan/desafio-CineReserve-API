from flask import Blueprint
import flask_restful as Rest

from .abstract_resource import AbstractResource
from ..repositories import SessaoRepository

class SessaoResource (AbstractResource):
    repository = SessaoRepository()
    methods = ["GET"]

resources = Blueprint("Sessoes", __name__, url_prefix="/sessoes")
api = Rest.Api(resources)
api.add_resource(SessaoResource, "/")