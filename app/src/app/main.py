from flask import Flask

from .error_handler import ErrorHandler
from .resources import resources
from . import app_singleton

def create_app():
    _app = Flask("CineReserve")
    ErrorHandler(_app)

    # TODO: Criar config do banco
    # app_singleton.db.init_app(_app)
    # app_singleton.migrate.init_app(_app, app_singleton.db)

    app_singleton.jwt.init_app(_app)
    app_singleton.basic_auth.init_app(_app)

    _app.register_blueprint(resources)
    return _app

def main():
    app = create_app()

    app.run(
        host="0.0.0.0",
        port=82,
        debug=True
    )

if __name__ == "__main__":
    main()