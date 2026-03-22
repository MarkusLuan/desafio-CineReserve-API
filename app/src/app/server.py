import argparse

from flask import Flask

from .error_handler import ErrorHandler
from .resources import resources
from .converters import JsonConverter
from . import app_singleton

def create_app(config_variante: str="dev"):
    _app = Flask("CineReserve")
    _app.config.from_object(f"app.config.{config_variante}")
    _app.json = JsonConverter(_app)
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
    paser = argparse.ArgumentParser(exit_on_error=False)
    paser.add_argument("--config", default="dev")
    config_object = paser.parse_known_args()[0].config

    app = create_app(config_object)

    app.run(
        host="0.0.0.0",
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )

if __name__ == "__main__":
    main()
