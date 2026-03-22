import datetime
import re

from werkzeug.exceptions import BadRequest

from ..exceptions import SqlInjectionException

def check_SQL_Injection (value):
    pattern = re.compile(r"(select|delete|create|drop|truncate|update)|([;\*])")
    if pattern.findall(str(value).lower()):
        raise SqlInjectionException()

def check_campos_obrigatorios (j: dict, campos: list):
    pattern_email = re.compile(r"(\w+)\@(\w{3,}[\w\.]{0,})")

    for campo in campos:
        # Valida se o campo foi informado
        if campo not in j:
            raise BadRequest(f"O campo '{campo}' não foi informado!")
        
        check_SQL_Injection(campo)
        check_SQL_Injection(j[campo])

        # Valida campo de e-mail
        if campo == "email" and not pattern_email.match(j[campo]):
            raise BadRequest("O endereço de e-mail é invalido!")
        
        # Validar campo de data
        if campo.startswith("dt_"):
            try:
                datetime.datetime.fromisoformat(j[campo])
            except Exception as e:
                raise BadRequest("A data não possui um formato valido") from e

def remover_campos_invalidos(j: dict, campos_validos: list):
    campos_json = list(j.keys())

    for campo in campos_json:
        if campo not in campos_validos:
            del j[campo]