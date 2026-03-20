from src.app.models.enums.genero_enum import GeneroEnum

class TestModels:
    def test_devera_testar_enum_genero(self):
        genero_acao = GeneroEnum.ACAO

        assert genero_acao.ordinal == 1
        assert str(genero_acao) == "Ação"

        genero_aventura = GeneroEnum.AVENTURA

        assert genero_aventura.ordinal == 2
        assert str(genero_aventura) == "Aventura"
