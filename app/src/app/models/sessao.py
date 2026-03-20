from .abstract_model import AbstractModel

from ..app_singleton import db

class Sessao (AbstractModel):
    __tablename__ = "Sessoes"
    fields = ["dt_lancamento, nome, descricao"]

    dt_sessao = db.Column(db.DateTime, nullable=False)
    quant_assentos = db.Column(db.Integer, default=0, nullable=False)
    filme_id = db.Column(db.Integer, db.ForeignKey("Usuarios.id"), nullable=False)

    filme = db.relationship("Filmes")