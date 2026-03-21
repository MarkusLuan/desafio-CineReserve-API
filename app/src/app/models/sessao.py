from .abstract_model import AbstractModel

from ..app_singleton import db

class Sessao (AbstractModel):
    __tablename__ = "Sessoes"
    fields = ["dt_sessao", "quant_assentos", "filme.uuid"]

    dt_sessao = db.Column(db.DateTime, nullable=False)
    quant_assentos = db.Column(db.Integer, default=0, nullable=False)
    filme_id = db.Column(db.Integer, db.ForeignKey("Filmes.id"), nullable=False)

    filme = db.relationship("Filme")
