import datetime

from flask.json.provider import DefaultJSONProvider

from ..models.enums.abstract_enum import AbstractEnum
from ..models.abstract_model import AbstractModel

class JsonConverter (DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        if isinstance(obj, AbstractEnum):
            return obj.label
        if isinstance(obj, AbstractModel):
            return obj.as_dict()

        return super().default(obj)