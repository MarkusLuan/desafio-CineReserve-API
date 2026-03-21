from sqlalchemy.orm import Query
from sqlalchemy import extract

from .abstract_filter import AbstractFilter

from ..filme import Filme
from ..enums import GeneroEnum
from ..dto_input import DTOInput

class FilmeFilter (AbstractFilter):
    titulo = DTOInput("titulo", str, "")
    genero = DTOInput("genero", GeneroEnum, None)
    ano_lancamento = DTOInput("ano_lancamento", int, 0)

    def make_filter(self, query: Query) -> Query:
        if self.titulo:
            query = query.filter(Filme.nome.like("%{}%".format(self.titulo.valor)))
        
        if self.genero:
            query = query.filter(Filme.genero == self.genero.valor)
        
        if self.ano_lancamento.valor > 0:
            query = query.filter(extract('year', Filme.dt_lancamento) == self.ano_lancamento.valor)
        return query