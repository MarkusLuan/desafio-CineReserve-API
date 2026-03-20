from flask import Flask, request
from flask import make_response
from werkzeug.exceptions import HTTPException

class ErrorHandler:
    def __init__(self, app: Flask):
        def __reportar_erro(erro: str, status_code: int):
            # TODO: Fazer sistemas de logs
            print(erro)

            res = make_response({
                "erro": True,
                "texto": str(erro)
            }, status_code)
            return res
        
        @app.errorhandler(401)
        def nao_autorizado (e):
            return __reportar_erro("Não autorizado!", 401)
        
        @app.errorhandler(405)
        def metodo_nao_permitido (e):
            return __reportar_erro(f"Não é permitido fazer '{request.method}' para este endpoint!", 405)
        
        @app.errorhandler(404)
        def nao_encontrado (e):
            return __reportar_erro("Não encontrado! Verifique o link e tente novamente!", 404)
        
        @app.errorhandler(HTTPException)
        def erro_http(e: HTTPException):
            return __reportar_erro(e.description or "", e.code or 500)
        
        @app.errorhandler(Exception)
        def erro_interno(e: Exception):
            return __reportar_erro(str(e), 500)
