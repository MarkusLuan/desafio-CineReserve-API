from flask import Flask

from .error_handler import ErrorHandler
from .resources import resources
from . import app_singleton

def create_app(config_variante: str="dev"):
    _app = Flask("CineReserve")
    _app.config.from_object(f"app.config.{config_variante}")
    ErrorHandler(_app)

    db_config = _app.config.get("DATABASE")
    if db_config:
        db_uri_str = "{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

        if db_config["ENGINE"] == "sqlite":
            db_uri_str = "{ENGINE}:///{NAME}"

        db_uri = db_uri_str.format(
            **db_config
        )

        _app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
        _app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

    app_singleton.db.init_app(_app)
    app_singleton.migrate.init_app(_app, app_singleton.db)

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