from flask import request, jsonify

from .abstract_resource import AbstractResource
from ..repositories import UsuarioRepository
from ..models import Usuario
from ..utils import seguranca_utils, validador_utils

class UsuarioResource (AbstractResource):
    repository = UsuarioRepository()
    methods = ["POST"]
    post_fields = ["dt_nascimento", "email", "nome", "senha"]

    def post(self):
        j = request.get_json()
        validador_utils.check_campos_obrigatorios(j, self.post_fields)
        validador_utils.remover_campos_invalidos(j, self.post_fields)

        usuario = Usuario(**j)
        usuario.senha = seguranca_utils.hash_senha(usuario.senha)

        res = self.repository.insert(usuario)
        return jsonify(res)