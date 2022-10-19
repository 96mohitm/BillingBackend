from datetime import datetime
from db import db
from models.order_model import OrderModel
from models.product_model import ProductModel
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class OrderItemModel(db.Model):
    __tablename__ = 'order_item'

    id = Column(db.Integer, primary_key=True)
    created_ts = Column(db.DateTime,nullable=False, default=datetime.utcnow())
    updated_ts = Column(db.DateTime,nullable=False, default=datetime.utcnow())
    order_id = Column(Integer, ForeignKey("order.id"))
    batch_id = Column(String)
    order = relationship("OrderModel", backref="order_item_list")
    product_id = Column(Integer, ForeignKey("product.id"))
    # quantity = Column(Float, nullable=False)


    def __init__(self, product_id, batch_id):
        self.product_id = int(product_id)
        self.batch_id = batch_id
        # self.quantity = quantity

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_id": self.product_id,
        }

    

