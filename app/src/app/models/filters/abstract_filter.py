import abc

from sqlalchemy.orm import Query

from ..dto_input import DTOInput

class AbstractFilter (abc.ABC):
    def __init__(self, *args, **kwargs) -> None:
        for k, v in kwargs.items():
            if hasattr(self, k):
                field = self.__getattribute__(k)
                if isinstance(field, DTOInput):
                    field.valor = v
    
    @abc.abstractmethod
    def make_filter(self, query: Query) -> Query:
        ...