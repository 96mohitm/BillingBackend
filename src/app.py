from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from manager.inventory_manager import InventoryListManager, InventoryManager
from manager.order_item_manager import OrderItemManager
from manager.order_manager import OrderListManager, OrderManager
from manager.product_manager import ProductListManager, ProductManager

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
api.add_resource(ProductManager, '/product')
api.add_resource(ProductListManager, '/product_list')
api.add_resource(OrderManager, '/order')
api.add_resource(OrderListManager, '/order_list')
api.add_resource(OrderItemManager, '/order_item_list')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
