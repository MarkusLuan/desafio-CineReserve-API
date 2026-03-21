import re
import enum
from typing import Type, TypeVar, Generic

from ..exceptions import SqlInjectionException, TipoInvalidoException

T = TypeVar("T")

class DTOInput (Generic[T]):
    chave: str
    tipo: Type[T]
    __valor: T
    default: T

    def __init__(self, chave: str, tipo: Type[T], default: T=None):
        self.chave = chave
        self.tipo = tipo
        self.default = default
        self.__valor = default

    def verificar_dado (self, value: T):
        pattern = re.compile(r"(select|delete|create|drop|truncate|update)|([;\*])")
        if pattern.findall(str(value).lower()):
            raise SqlInjectionException()
        
        if not isinstance(value, self.tipo):
            v = str(value)
            if self.tipo == int and v.isdigit():
                value = int(v)
            elif self.tipo == str:
                value = str(v)
            elif issubclass(self.tipo, enum.Enum):
                value = self.tipo[v]
            else:
                raise TipoInvalidoException(self.tipo, type(value))
        return value

    @property
    def valor(self):
        self.verificar_dado(self.__valor)
        return self.__valor
    
    @valor.setter
    def valor(self, value: T):
        value = self.verificar_dado(value)
        self.__valor = value