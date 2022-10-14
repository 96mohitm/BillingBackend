import datetime
from db import db


class ProductModel(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    created_ts = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    updated_ts = db.Column(db.Datetime,nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(140),nullable=False)
    description = db.Column(db.String(1000),nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def json(self):
        return {
            'id': self.id,
            'created_ts': self.created_ts.strftime('%Y/%m/%d'),
            'updated_ts': self.updated_ts.strftime('%Y/%m/%d'),
            'name': self.name,
            'description': self.description
        }

    def __repr__(self):
        pass

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
