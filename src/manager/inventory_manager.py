from flask_restful import Resource
from models.inventory_model import InventoryModel


class InventoryManager(Resource):

    def post(self):
        inventory = InventoryModel(2)
        try:
            inventory.save_to_db()
        except:
            return {"message": "An error occurred inserting the post."}, 500

        return inventory.json(), 201


class InventoryListManager(Resource):

    def get(self):
        return {'posts': list(map(lambda x: x.json(), InventoryModel.query.all()))}
