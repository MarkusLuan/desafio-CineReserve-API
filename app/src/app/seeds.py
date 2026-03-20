import argparse
import random
import json

from . import server

from app.models import Filme, Sessao
from app.models.enums import GeneroEnum
from app.app_singleton import db

def seed(_config_object: str):
    _app = server.create_app(_config_object)

    filmes = []
    with open("movies.json", "r", encoding="utf-8") as f:
        j = json.load(f)

        for r in j:
            r["genero"] = GeneroEnum[r["genero"]]
            filmes.append(Filme(**r))

    # Gerar sessões aleatórias
    sessoes = []
    for a in range(0, 2000):
        sessao = Sessao(
            dt_sessao = f'2026-{random.randint(3, 12)}-{random.randint(1, 30)}',
            quant_assentos = random.randint(20, 150),
            filme_id = random.randint(1, len(filmes))
        )

        sessoes.append(sessao)

    with _app.app_context():
        if not Filme.query.first() and not Sessao.query.first():
            db.session.add_all(filmes + sessoes)
            db.session.commit()
    
            print("Banco de dados populado com sucesso!")
        else:
            print(".")

def main():
    paser = argparse.ArgumentParser(exit_on_error=False)
    paser.add_argument("--config", default="dev")
    config_object = paser.parse_known_args()[0].config

    seed(config_object)

if __name__ == "__main__":
    main()