import dataclasses

from sqlalchemy.orm import Query
from sqlalchemy import extract

from .abstract_filter import AbstractFilter

from ..filme import Filme
from ..enums import GeneroEnum
from .dto_filter import DTOFilter

class FilmeFilter (AbstractFilter):
    def __init__(self, *args, **kwargs) -> None:
        self.titulo = DTOFilter("titulo", str, "")
        self.genero = DTOFilter("genero", GeneroEnum, None)
        self.ano_lancamento = DTOFilter("ano_lancamento", int, 0)

        super().__init__(*args, **kwargs)

    def make_filter(self, query: Query) -> Query:
        if self.titulo:
            query = query.filter(Filme.nome.like("%{}%".format(self.titulo.valor)))
        
        if self.genero:
            query = query.filter(Filme.genero == self.genero.valor)
        
        if self.ano_lancamento.valor > 0:
            query = query.filter(extract('year', Filme.dt_lancamento) == self.ano_lancamento.valor)
        return query