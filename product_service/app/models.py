from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)
    return db

def create_tables(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db.metadata.create_all(engine)
    return engine

class Product(db.Model):
    id = db.column(db.Integer,primary_key=True)
    name = db.column(db.string(255),unique=True,nullable=False)
    slug = db.column(db.string(255),unique=True,nullable=False)
    price = db.column(db.Integer,nullable=False)
    image = db.column(db.string(255),unique=False,nullable=True)
    dateAdded = db.column(db.dateTime,default=datetime.utcnow)
    dateUpdated = db.column(db.dateTime,default=datetime.utcnow)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'price': self.price,
            'image': self.image
        }