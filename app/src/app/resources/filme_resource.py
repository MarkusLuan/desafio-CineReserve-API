from flask import Blueprint
import flask_restful as Rest

from .abstract_resource import AbstractResource
from ..repositories import FilmeRepository

class FilmeResource (AbstractResource):
    repository = FilmeRepository()
    methods = ["GET"]

resources = Blueprint("Filmes", __name__, url_prefix="/filmes")
api = Rest.Api(resources)
api.add_resource(FilmeResource, "/")