from .abstract_enum import AbstractEnum

class StatusAssentoEnum (AbstractEnum):
    DISPONIVEL = (1, "Disponível")
    RESERVADO = (2)
    COMPRADO = (3)