from datetime import datetime
from db import db


class ProductModel(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    created_ts = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_ts = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    name = db.Column(db.String(140), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    unit = db.Column(db.String(140), nullable=False)

    def __init__(self, name, description, unit):
        self.name = name
        self.description = description
        self.unit = int(unit)
    
    def json(self):
        return {
            'id': self.id,
            'created_ts': self.created_ts.strftime('%Y/%m/%d'),
            'updated_ts': self.updated_ts.strftime('%Y/%m/%d'),
            'name': self.name,
            'description': self.description,
            "unit": self.unit,
        }

    def __repr__(self):
        return '<id {}>'.format(self.id)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
