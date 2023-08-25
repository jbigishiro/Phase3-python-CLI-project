from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db')

Base = declarative_base()

class Supplier(Base):
    __tablename__ = "suppliers"

    id= Column( Integer(), primary_key=True)

