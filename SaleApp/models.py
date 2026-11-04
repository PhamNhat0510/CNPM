from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
import json

from SaleApp import app,db

class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=True, unique=True)
    def __str__(self):
        return self.name
class Category(Base):
    products=relationship('Product',backref='category',lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=True, unique=True)
    price=Column(Float,default=0.0)
    cate_id=Column(Integer,ForeignKey(Category.id))
    image=Column(String(3000),default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRb4wMKcZskt8e9-ePQbZM7C0j6Jmq6MQfMOgWvIokYxA&s=10")
    def __str__(self):
        return self.name

if __name__=='__main__':
    with app.app_context():
        db.create_all()
        # c1=Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # c3 = Category(name="Laptop")
        # db.session.add_all([c1,c2,c3])

        with open("data/products.json", encoding="utf-8") as f:
            prods = json.load(f)

            for p in prods:
                db.session.add(Product(**p))
            db.session.commit()