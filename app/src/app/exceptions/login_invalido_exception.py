class LoginInvalidoException (BaseException):
    def __init__(self):
        super().__init__(("O Usuário ou a senha estão invalidos!"))