from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from manager.inventory_manager import InventoryListManager, InventoryManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///billing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'mohit'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()



api.add_resource(InventoryManager, '/')
api.add_resource(InventoryListManager, '/inventory_list')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
