import abc

from sqlalchemy.orm import Query

from .dto_filter import DTOFilter

class AbstractFilter (abc.ABC):
    def __init__(self, *args, **kwargs) -> None:
        for k, v in kwargs.items():
            if hasattr(self, k):
                field = self.__getattribute__(k)
                if isinstance(field, DTOFilter):
                    field.valor = v
    
    @abc.abstractmethod
    def make_filter(self, query: Query) -> Query:
        ...
    
    def clear(self):
        for k in self.__dict__.keys():
            field = self.__getattribute__(k)
            if isinstance(field, DTOFilter):
                field.valor = field.default
