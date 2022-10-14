from db import db
from datetime import datetime

class InventoryModel(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    created_dt = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    quantity = db.Column(db.Integer)
    # price = db.Column(db.Float)

    def __init__(self, quantity):
        self.quantity = quantity

    def json(self):
        return {
            'id': self.id,
            'created_dt': self.created_dt.strftime('%Y/%m/%d'),
            'quantity': self.quantity
        }

    def __repr__(self):
            return '<id {}>'.format(self.id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
