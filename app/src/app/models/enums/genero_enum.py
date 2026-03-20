# pylint: disable=C0325

from .abstract_enum import AbstractEnum

class GeneroEnum (AbstractEnum):
    ACAO = (1, "Ação")
    AVENTURA = (2)
    SUSPENSE = (3)
    COMEDIA = (4, "Comédia")
    DRAMA = (5)
    DOCUMENTARIO = (6, "Documentário")
    FICCAO = (7, "Ficção")
    ROMANCE = (8)
    TERROR = (9)
    MUSICAL = (10)
