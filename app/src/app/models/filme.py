from .enums import GeneroEnum
from .abstract_model import AbstractModel

from ..converters import EnumConverter
from ..app_singleton import db

class Filme (AbstractModel):
    __tablename__ = "Filmes"
    fields = ["ano_lancamento, nome, descricao, idade_min, genero, capa"]

    ano_lancamento = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(250), nullable=False)
    descricao = db.Column(db.String(350), nullable=False)
    idade_min = db.Column(db.Integer, default=0, nullable=False)
    genero = db.Column(EnumConverter(GeneroEnum), nullable=False)

    # TODO: Se sobrar tempo add coluna do elenco também

    @property
    def capa(self):
        # TODO: Implementar para devolver a url da imagem
        return ""
