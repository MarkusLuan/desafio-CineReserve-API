from flask import request, jsonify

from .abstract_resource import AbstractResource
from ..repositories import UsuarioRepository
from ..models import Usuario
from ..utils import seguranca_utils

class UsuarioResource (AbstractResource):
    repository = UsuarioRepository()
    methods = ["POST"]

    def post(self):
        j = request.get_json()

        usuario = Usuario(**j)
        usuario.senha = seguranca_utils.hash_senha(usuario.senha)

        res = self.repository.insert(usuario)
        return jsonify(res)