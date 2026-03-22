import base64
import hashlib

def toBase64(texto: str):
    """ Função codifca o texto em base64 """

    buffer = texto.encode("utf-8")
    
    return str(
        base64.b64encode(buffer),
        "utf-8"
    )

def fromBase64(texto: str):
    """ Função decodifca o texto de base64 """

    return str(base64.b64decode(texto),
        "utf-8"
    )

def hash_senha(texto: str):
    """ Função para encriptar senhas """

    # Embaraça o texto com outros caracteres antes de criptografar
    texto = f"h68soXIw90h6{texto}_MtP9S32.Y5Qf5m1"
    buffer = texto.encode("utf-8")
    _hash = hashlib.md5(buffer)
    
    return _hash.hexdigest()
