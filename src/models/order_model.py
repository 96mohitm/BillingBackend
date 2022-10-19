from datetime import datetime
from db import db
from sqlalchemy.orm import relationship


class OrderModel(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    created_ts = db.Column(db.DateTime,nullable=False, default=datetime.utcnow())
    updated_ts = db.Column(db.DateTime,nullable=False, default=datetime.utcnow())
    customer_name = db.Column(db.String(140),nullable=False)
    contact = db.Column(db.String(140),nullable=False)
    discount_percentage = db.Column(db.Integer, default=0)

    def __init__(self, customer_name, contact, discount_percentage):
        self.customer_name = customer_name
        self.contact = contact
        self.discount_percentage = discount_percentage
        
    def json(self):
        return {
            'id': self.id,
            'created_ts': self.created_ts.strftime('%Y/%m/%d'),
            'updated_ts': self.updated_ts.strftime('%Y/%m/%d'),
            'customer_name': self.customer_name,
            'contact': self.contact,
            # 'item_list': self.order_item_list
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    


    
