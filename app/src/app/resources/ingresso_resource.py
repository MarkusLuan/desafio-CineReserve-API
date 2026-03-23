from flask import request, jsonify
import flask_jwt_extended as jwt

from .abstract_resource import AbstractResource
from ..repositories import IngressoRepository, UsuarioRepository

class IngressoResource (AbstractResource):
    repository = IngressoRepository()
    methods = ["GET"]

    @jwt.jwt_required()
    def get(self):
        usuario_repository = UsuarioRepository()
        usuario = usuario_repository.get_logged_user()
        if not usuario:
            raise Exception ("Deve estar logado para esta operação!")

        args = { k: v for k, v in request.args.items() }
        args["uuid_usuario"] = str(usuario.uuid)
        res = self.repository.get(**args)
        return jsonify(res)
    
    #TODO: Mover Confirmação de reserva para cá