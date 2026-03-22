import datetime
import uuid
import random

import redis
from flask import Blueprint, request, jsonify, abort
import flask_jwt_extended as jwt

from ..models.enums import StatusAssentoEnum
from ..models import Ingresso, Sessao, Usuario
from ..repositories import IngressoRepository, UsuarioRepository, SessaoRepository
from ..utils import validador_utils
from .. import app_singleton

resources = Blueprint("assentos", __name__, url_prefix="/assentos")
repository = IngressoRepository()
usuario_repository = UsuarioRepository()
sessao_repository = SessaoRepository()

redis_cli = redis.Redis(host="localhost", port=6379, db=0)

@resources.before_request
@jwt.jwt_required()
def before_request():
    ...

@resources.route("/<uuid:uuid_sessao>", methods=["GET"])
def listar_assentos(uuid_sessao: uuid.UUID):
    validador_utils.check_SQL_Injection(uuid_sessao)
    res = repository.get_assentos(uuid_sessao)
    return jsonify(res)

@resources.route("/<uuid:uuid_sessao>/<int:indice_assento>", methods=["GET"])
def selecionar_assento(uuid_sessao: uuid.UUID, indice_assento: int):
    usuario = usuario_repository.get_logged_user()
    if not usuario:
        return abort(401)
    
    if not repository.is_assento_disponivel (uuid_sessao, indice_assento):
        raise Exception ("O assento já está ocupado!")

    sessao = sessao_repository.get_by_uuid(uuid_sessao)
    if not sessao:
        return abort(404)

    pre_reserva = redis_cli.set(repository.key_reserva(uuid_sessao, indice_assento), str(usuario.uuid), ex=10*60, nx=True)
    if pre_reserva:
        return jsonify({
            "erro": False,
            "texto": "Reservado com sucesso!"
        })
    else:
        raise Exception ("O assento já está reservado!")

@resources.route("/<uuid:uuid_sessao>/<int:indice_assento>", methods=["POST"])
def reservar_assento(uuid_sessao: uuid.UUID, indice_assento: int):
    if not repository.is_assento_disponivel (uuid_sessao, indice_assento):
        raise Exception ("O assento já está ocupado!")

    sessao = sessao_repository.get_by_uuid(uuid_sessao)
    if not sessao:
        return abort(404)
    sessao_id = sessao.id
    
    usuario = usuario_repository.get_logged_user()
    if not usuario:
        raise abort(401)
    usuario_id = usuario.id

    ingresso = Ingresso(
        dt_reserva = datetime.datetime.now().isoformat(),
        codigo = str(random.randint(1, 800000)),
        assento = indice_assento,
        status_assento = StatusAssentoEnum.COMPRADO,
        sessao_id = sessao_id,
        usuario_id = usuario_id,
    )
    repository.insert(ingresso)

    return jsonify(ingresso)