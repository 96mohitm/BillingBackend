from db import db
from sqlalchemy.dialects.postgresql import JSON


class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)

    def __init__(self, quantity):
        self.quantity = quantity

    def __repr__(self):
        return '<id {}>'.format(self.id)
