from .enums import StatusAssentoEnum
from .abstract_model import AbstractModel

from ..converters import EnumConverter
from ..app_singleton import db

class Ingresso (AbstractModel):
    __tablename__ = "Ingressos"
    fields = ["dt_reserva, codigo, assento, sessao.uuid"]

    dt_reserva = db.Column(db.DateTime, nullable=False)
    codigo = db.Column(db.String(100), unique=True, nullable=False)
    assento = db.Column(db.Integer, nullable=False)
    status_assento= db.Column(EnumConverter(StatusAssentoEnum), nullable=False)
    sessao_id = db.Column(db.Integer, db.ForeignKey("Sessoes.id"), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("Usuarios.id"), nullable=False)

    sessao = db.relationship("Sessoes")
    usuario = db.relationship("Usuarios")
