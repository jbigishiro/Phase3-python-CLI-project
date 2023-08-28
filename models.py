from sqlalchemy import Column, Integer, create_engine, ForeignKey, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = create_engine('sqlite:///database.db')
engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Supplier(Base):
    __tablename__ = "suppliers"

    id= Column( Integer(), primary_key=True)
    name= Column(String(), unique=True)
    address= Column(String(), unique=True)
    products= relationship('Product', backref=backref('supplier'))

    def __repr__(self):
        return f'Supplier(id={self.id}, ' + \
            f'Name={self.name}, ' + \
            f'Address={self.address})'
    
    @classmethod
    def search_supplier_by_id(cls, supplier_id):
        supplier = session.query(cls).filter(cls.id == supplier_id).first()
        return supplier

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
    
    @classmethod
    def show_all_products(cls):
        return session.query(cls).all()
    
    @classmethod
    def show_product_by_name(cls, product_name):
        return session.query(cls).filter(Product.name==product_name).all()
    
    @classmethod
    def add_product(cls, name, unit_price, supplier_id):
        item = cls(name=name, unit_price=unit_price, supplier_id=supplier_id)
        session.add(item)
        session.commit()
        return item
    
    @classmethod
    def delete_item_by_id(cls, product_id):
        product = session.query(Product).filter(Product.id == product_id).first()
        session.delete(product)
        session.commit()
