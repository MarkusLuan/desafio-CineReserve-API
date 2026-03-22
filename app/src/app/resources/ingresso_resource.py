from flask import jsonify
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
        
        res = self.repository.get_meus_ingressos(usuario)
        return jsonify(res)
    
    #TODO: Mover Confirmação de reserva para cá