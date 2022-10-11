from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Inventory(Resource):
    def get(self):
        return {"test": "test"}


api.add_resource(Inventory, '/')


if __name__ == '__main__':
    app.run(debug=True)
