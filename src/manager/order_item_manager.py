from flask_restful import Resource

from models.order_item_model import OrderItemModel


class OrderItemManager(Resource):
    def get(self):
        return {"order_item_list": list(map(lambda x: x.json(), OrderItemModel.query.all()))}