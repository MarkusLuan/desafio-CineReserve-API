from uuid import uuid4

from ..app_singleton import db

class AbstractModel (db.Model):
    __abstract__ = True
    __table__args__ = { "sqlite_autoincrement": True }
    fields: list[str] = []

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    uuid = db.Column(db.String(36), default=lambda: str(uuid4()), unique=True, nullable=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def as_dict(self):
        j = {
            "uuid": self.uuid
        }

        for field in self.fields:
            j[field] = self.__getattribute__(field)

        return j