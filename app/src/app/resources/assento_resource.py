import datetime
import uuid
import random

from flask import Blueprint, request, jsonify
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
    return "ok"

@resources.route("/<uuid:uuid_sessao>/<int:indice_assento>", methods=["POST"])
def reservar_assento(uuid_sessao: uuid.UUID, indice_assento: int):
    if not repository.is_assento_disponivel (uuid_sessao, indice_assento):
        raise Exception ("O assento já está ocupado!")

    session = app_singleton.db.session
    query = session.query(Sessao)
    query = query.filter(Sessao.uuid == str(uuid_sessao))
    sessao = query.first()
    if not sessao:
        raise Exception ("Sessão de Filme invalida!")
    sessao_id = sessao.id
    session.close()
    
    usuario = usuario_repository.get_logged_user()
    if not usuario:
        raise Exception ("Usuário inválido!")
    usuario_id = usuario.id

    print("Cheguei")

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