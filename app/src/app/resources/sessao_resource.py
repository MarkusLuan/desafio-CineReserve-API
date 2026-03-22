import uuid

from flask import request, jsonify

from .abstract_resource import AbstractResource
from ..repositories import SessaoRepository

class SessaoResource (AbstractResource):
    repository = SessaoRepository()
    methods = ["GET"]

    def get(self, uuid_filme: uuid.UUID, *args, **kwargs):
        args = request.args.__dict__
        args["uuid_filme"] = uuid_filme
        res = self.repository.get(**args)
        return jsonify(res)