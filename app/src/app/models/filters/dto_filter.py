import datetime
import enum
import uuid
from typing import Type, TypeVar, Generic

from ...exceptions import TipoInvalidoException, ParametroObrigatorioException
from ...utils import validador_utils

T = TypeVar("T")

class DTOFilter (Generic[T]):
    chave: str
    tipo: Type[T]
    __valor: T
    default: T
    is_obrigatorio: bool

    def __init__(self, chave: str, tipo: Type[T], default: T=None, is_obrigatorio: bool=False):
        self.chave = chave
        self.tipo = tipo
        self.default = default
        self.__valor = default
        self.is_obrigatorio = is_obrigatorio

    def verificar_dado (self, value: T):
        validador_utils.check_SQL_Injection(value)
        
        try:
            if value is None:
                if self.is_obrigatorio:
                    raise ParametroObrigatorioException(self.chave)
                return None

            if not isinstance(value, self.tipo):
                v = str(value)
                if self.tipo == int and v.isdigit():
                    value = int(v)
                elif self.tipo == datetime.datetime:
                    value = datetime.datetime.fromisoformat(value)
                elif self.tipo == uuid.UUID:
                    value = uuid.UUID(v)
                elif self.tipo == str:
                    value = str(v)
                elif issubclass(self.tipo, enum.Enum):
                    value = self.tipo[v.upper()]
                else:
                    raise TipoInvalidoException(self.tipo, type(value))
        except Exception as e:
            raise TipoInvalidoException(self.tipo, type(value)) from e
        return value
    
    def __bool__(self):
        return bool(self.valor)

    @property
    def valor(self):
        self.verificar_dado(self.__valor)
        return self.__valor
    
    @valor.setter
    def valor(self, value: T):
        value = self.verificar_dado(value)
        self.__valor = value