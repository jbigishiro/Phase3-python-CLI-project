from sqlalchemy import Column, Integer, create_engine, ForeignKey, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///database.db')

Base = declarative_base()

class Supplier(Base):
    __tablename__ = "suppliers"

    id= Column( Integer(), primary_key=True)
    name= Column(String())
    address= Column(String())
    products= relationship('Product', backref('supplier'))

    def __repr__(self):
        return f'Supplier(id={self.id}, ' + \
            f'Name={self.name}, ' + \
            f'Address={self.address})'

class Product(Base):
    __tablename__ = "products"

    id= Column( Integer(), primary_key=True)
    name= Column(String())
    unit_price= Column(Float())
    supplier_id= Column(Integer(), ForeignKey('suppliers.id'))

    def __repr__(self):
        return f'Product(id={self.id}, ' + \
            f'Name={self.name}, ' + \
            f'Supplier_id={self.supplier_id})'

