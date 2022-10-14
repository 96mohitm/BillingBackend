from flask_restful import Resource

from models.product_model import ProductModel


class ProductManager(Resource):

    def get(self, id):
        return ProductModel.find_by_id(id)


    def post(self, name, description):
        if ProductModel.find_by_name(name):
            return {'message': "An product with name '{}' already exists.".format(name)}, 400
        product = ProductModel(name, description)

        try:
            product.save_to_db()
        except:
            return {"message": "An error occurred inserting the post."}, 500


        return product.json(), 201
