import pytest

from src.app.models.filters.filme_filter import FilmeFilter
from src.app.exceptions import SqlInjectionException, TipoInvalidoException

class TestFilters:
    def test_devera_retornar_erro_tentativa_sql_injection(self):
        with pytest.raises(SqlInjectionException) as r:
            f = FilmeFilter(**{
                "titulo": "SELECT * FROM table"
            })

            f = FilmeFilter(**{
                "titulo": "UPDATE table SET t = 123"
            })
    
    def test_devera_retornar_erro_tipo_invalido(self):
        with pytest.raises(TipoInvalidoException) as r:
            f = FilmeFilter(**{
                "titulo": 1234
            })

            f = FilmeFilter(**{
                "titulo": "2323123",
                "genero": "acokda"
            })
    
    def test_devera_funcionar_sem_erros(self):
        f = FilmeFilter(**{
            "titulo": "Duro de Matar"
        })

        f = FilmeFilter(**{
            "titulo": "Anaconda",
            "genero": "SUSPENSE"
        })