import uuid

from flask import request, jsonify
from werkzeug.exceptions import BadRequest

from .abstract_resource import AbstractResource
from ..repositories import IngressoRepository
from ..utils import validador_utils

class AssentoResource (AbstractResource):
    repository = IngressoRepository()
    methods = ["GET"]

    def get(self):
        uuid_sessao = request.args.get("uuid_sessao", type=uuid.UUID)
        if not uuid_sessao:
            raise BadRequest("O 'uuid_sessao' não foi informado!")
        
        validador_utils.check_SQL_Injection(uuid_sessao)
        res = self.repository.get_assentos(uuid_sessao)
        return jsonify(res)