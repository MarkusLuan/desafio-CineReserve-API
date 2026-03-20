from . import server
from . import app_singleton
from . import models

import argparse

def migrate(_config_object: str):
    _app = server.create_app(_config_object)

    with _app.app_context():
        app_singleton.db.drop_all()
        app_singleton.db.create_all()
        print("Banco de dados criado com sucesso!")

def main ():
    paser = argparse.ArgumentParser(exit_on_error=False)
    paser.add_argument("--config", default="dev")
    config_object = paser.parse_known_args()[0].config

    migrate(config_object)

if __name__ == "__main__":
    main()