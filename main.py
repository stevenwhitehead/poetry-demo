from flask import Flask, request
from flask_restful import Resource, Api
from ibm_db import *

app = Flask(__name__)
api = Api(app)
port = 8080

class topic_tags(Resource):
    def get(self):
        return {'hello': 'world world'}

api.add_resource(topic_tags, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(port))
