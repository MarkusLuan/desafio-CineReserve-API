class ParametroObrigatorioException (BaseException):
    def __init__(self, parametro: str):
        super().__init__(f"O parâmetro '{parametro}' é obrigatório!")