from flask import request, jsonify, abort
import flask_restful as Rest

from ..repositories.abstract_repository import AbstractRepository

class AbstractResource (Rest.Resource):
    repository = AbstractRepository()
    methods = []

    def get (self):
        args = request.args
        res = self.repository.get(**args)
        return jsonify(res)
    
    def post (self):
        raise NotImplementedError()
    
    def dispatch_request(self, *args, **kwargs):
        if not self.methods or (request.method not in self.methods):
            abort(405)

        return super().dispatch_request(*args, **kwargs)