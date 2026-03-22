import flask_jwt_extended as jwt

from .abstract_repository import AbstractRepository
from ..models import Usuario
from ..utils import seguranca_utils
from ..exceptions import LoginInvalidoException
from .. import app_singleton

class UsuarioRepository (AbstractRepository [Usuario]):
    model = Usuario
    is_paginate = False
    is_can_insert = True

    def check_ja_existente(self, entity: Usuario):
        usuario = self.model.query.filter(self.model.email == entity.email).first()
        if usuario:
            raise Exception("Usuário já existente!")
    
    def fazer_login (self, email: str, senha: str):
        session = app_singleton.db.session
        query = session.query(self.model)
        usuario = query.filter(self.model.email == email).first()

        if not usuario or usuario.senha != seguranca_utils.hash_senha(senha):
            raise LoginInvalidoException()
        
        usuario.senha = None
        return usuario

    def get_logged_user (self):
        identity = jwt.get_jwt_identity()
        
        session = app_singleton.db.session
        query = session.query(self.model)
        usuario = query.filter(self.model.uuid == identity).first()

        if usuario:
            usuario.senha = None
        return usuario