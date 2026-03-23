from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_basicauth import BasicAuth
import redis

db = SQLAlchemy()
migrate = Migrate()

jwt = JWTManager()
basic_auth = BasicAuth()
redis_cli = redis.Redis(host="localhost", port=6379, db=0)