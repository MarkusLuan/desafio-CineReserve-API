from .enums import GeneroEnum
from .abstract_model import AbstractModel

from ..converters import EnumConverter
from ..app_singleton import db

class Filme (AbstractModel):
    __tablename__ = "Filmes"
    fields = ["dt_lancamento", "nome", "descricao", "idade_min", "genero", "capa"]

    dt_lancamento = db.Column(db.Date, nullable=False)
    nome = db.Column(db.String(250), nullable=False)
    descricao = db.Column(db.String(1000), nullable=False)
    idade_min = db.Column(db.Integer, default=0, nullable=False)
    genero = db.Column(EnumConverter(GeneroEnum), nullable=False)
    capa = db.Column(db.String(250), nullable=True)
