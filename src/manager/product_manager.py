from flask import request
from flask_restful import Resource, reqparse

from models.product_model import ProductModel


class ProductManager(Resource):

    def post(self):
        data = request.get_json()
        if ProductModel.find_by_name(data['name']):
            name = data['name']
            return {'message': "An product with name '{}' already exists.".format(name)}, 400
        
        product = ProductModel(**data)

        try:
            product.save_to_db()
        except:
            return {"message": "An error occurred inserting the post."}, 500


        return product.json(), 201

    # Gets a product using product_id
    def get(self):
        args = request.args
        try:
            return ProductModel.find_by_id(int(args['product_id'])).json()
        except:
            return {"message": "Product was not found."}, 500

class ProductListManager(Resource):

    def get(self):
        return {'products': list(map(lambda x: x.json(), ProductModel.query.all()))}
