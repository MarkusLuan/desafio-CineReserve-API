class SqlInjectionException (BaseException):
    def __init__(self):
        super().__init__("Uma tentativa de SQL Injection foi detectada!")