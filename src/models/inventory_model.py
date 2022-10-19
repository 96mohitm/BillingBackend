from sqlalchemy import ForeignKey, String
from db import db
from datetime import datetime

class InventoryModel(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, ForeignKey('product.id'), nullable=False)
    batch_id = db.Column(String)
    created_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    quantity = db.Column(db.Integer, nullable=False)
    price_per_quantity = db.Column(db.Float, nullable=False)

    def __init__(self, product_id, batch_id, quantity, price_per_quantity):
        self.product_id = product_id
        self.batch_id = batch_id
        self.quantity = quantity
        self.price_per_quantity = price_per_quantity

    def json(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            "batch_id": self.batch_id,
            'created_dt': self.created_dt.strftime('%Y/%m/%d'),
            'quantity': self.quantity,
            'price_per_quantity': self.price_per_quantity
        }

    def __repr__(self):
            return '<id {}>'.format(self.id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self):
        db.session.commit()
    
    @classmethod
    def find_by_product_id_batch_id(cls, product_id, batch_id):
        return cls.query.filter_by(product_id=product_id, batch_id=batch_id).first()
