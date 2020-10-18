from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "Efe": {
        "name": "Efe",
        "age": 12,
    },
    "Guy": {
        "name": "Guy",
        "age": 64,
    }
}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)