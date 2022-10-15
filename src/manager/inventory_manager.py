from flask import request
from flask_restful import Resource
from models.inventory_model import InventoryModel


class InventoryManager(Resource):

    def post(self):
        inventory_json = request.get_json()
        inventory = InventoryModel(
            product_id=inventory_json.get('product_id'),
            quantity=inventory_json.get('quantity'),
            price_per_quantity=inventory_json.get('price_per_quantity'))
        try:
            inventory.save_to_db()
        except Exception as ex:
            return {"message": "An error occurred inserting the post.", "error": str(ex)}, 500

        return inventory.json(), 201


class InventoryListManager(Resource):

    def get(self):
        return {'posts': list(map(lambda x: x.json(), InventoryModel.query.all()))}
