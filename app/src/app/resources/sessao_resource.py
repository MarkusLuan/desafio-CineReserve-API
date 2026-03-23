import uuid

from flask import request, jsonify

from .abstract_resource import AbstractResource
from ..repositories import SessaoRepository

class SessaoResource (AbstractResource):
    repository = SessaoRepository()
    methods = ["GET"]

    def get(self, uuid_filme: uuid.UUID, *args, **kwargs):
        args = { k: v for k, v in request.args.items() }
        args["uuid_filme"] = str(uuid_filme)
        res = self.repository.get(**args)
        return jsonify(res)