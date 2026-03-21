class TipoInvalidoException (BaseException):
    def __init__(self, dado_esperado: type, dado_informado: type):
        super().__init__(f"Foi passado um tipo de dado invalído!\nFoi passado '{dado_informado}', mas esperava '{dado_esperado}'")

        self.dado_esperado = dado_esperado
        self.dado_informado = dado_informado