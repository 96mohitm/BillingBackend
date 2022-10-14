from flask_restful import Resource, reqparse

from models.product_model import ProductModel


class ProductManager(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('description')

    def post(self):
        data = ProductManager.parser.parse_args()
        if ProductModel.find_by_name(data['name']):
            name = data['name']
            return {'message': "An product with name '{}' already exists.".format(name)}, 400
        
        product = ProductModel(**data)

        try:
            product.save_to_db()
        except:
            return {"message": "An error occurred inserting the post."}, 500


        return product.json(), 201

class ProductListManager(Resource):

    def get(self):
        return {'products': list(map(lambda x: x.json(), ProductModel.query.all()))}
