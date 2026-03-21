from .abstract_repository import AbstractRepository
from ..models import Usuario

class UsuarioRepository (AbstractRepository [Usuario]):
    model = Usuario
    is_paginate = False
    is_can_insert = True

    def check_ja_existente(self, entity: Usuario):
        usuario = self.model.query.filter(self.model.email == entity.email).first()
        if usuario:
            raise Exception("Usuário já existente!")