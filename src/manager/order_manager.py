from flask import request
from flask_restful import Resource
from builder.order_builder import OrderBuilder
from controller.order_controller import OrderController
from exception.out_of_stock import OutOfStockException

from models.order_model import OrderModel

class OrderManager(Resource):
    def post(self):
        try:
            order_json = request.get_json()
            order_meta_data = OrderBuilder.order_meta_data_builder(order_json)
            order_item_list = OrderBuilder.order_item_list_builder(order_json)
            order_controller = OrderController()
            order = order_controller.place_order(order_meta_data, order_item_list)
        except OutOfStockException as ex:
            return {"message": str(ex)}, 400
        except Exception as ex:
            return {"message": "An error occurred inserting order", "error": str(ex)}, 500
        return order.json(), 201

    # gets a order using order_id
    def get(self):
        args = request.args
        try:
            return OrderModel.find_by_id(int(args['order_id'])).json()
        except:
            return { "message": "Order was not found"}, 500

class OrderListManager(Resource):

    def get(self):
        return {'orders': list(map(lambda x: x.json(), OrderModel.query.all()))}
