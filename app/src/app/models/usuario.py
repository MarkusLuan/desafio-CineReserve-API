from .abstract_model import AbstractModel

from ..app_singleton import db

class Usuario (AbstractModel):
    __tablename__ = "Usuarios"
    fields = ["dt_nascimento", "nome", "email"]

    dt_nascimento = db.Column(db.Date, nullable=False)
    nome = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
