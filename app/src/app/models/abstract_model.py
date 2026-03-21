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
            if "." in field:
                sub_fields = field.split(".")
                
                index_field = 0
                sub_j = j
                sub_field = self
                for sf in sub_fields:
                    sub_field = sub_field.__getattribute__(sf)

                    sub_j[sf] = {}
                    if index_field == len(sub_fields) -1:
                        sub_j[sf] = sub_field

                    sub_j = sub_j[sf]
                    index_field += 1
            else:
                j[field] = self.__getattribute__(field)

        return j