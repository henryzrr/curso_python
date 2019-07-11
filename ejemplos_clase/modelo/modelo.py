from sqlalchemy import MetaData, Table, Column, String, Integer, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from .conexion import Database

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Numeric(12, 2))

    venta = relationship("Venta", back_populates="product")

    @classmethod
    def all(cls):
        dataBase = Database()
        meta = MetaData()
        products = Table('product', meta,
                         Column('name'),
                         Column('price'))
        data = dataBase.connection.execute(products.select())
        return data

    def save(self):
        dataBase = Database()
        session = Session(bind=dataBase.connection)
        session.add(self)
        session.commit()

    def delete(cls, prod_name):
        dataBase = Database()
        session = Session(bind=dataBase.connection)
        product_data = session.query(Product).filter(Product.name == prod_name).first()
        session.delete(product_data)
        session.commit()

    def updateProduct(self, new_name, new_price):
        dataBase = Database()
        session = Session(bind=dataBase.connection)
        dataToUpdate = {
            Product.name: new_name,
            Product.price: new_price
        }
        customerData = session.query(Product).filter(Product.name == self.name)
        customerData.update(dataToUpdate)
        session.commit()

    def getProduct(self, name):
        dataBase = Database()
        session = Session(bind=dataBase.connection)
        customerData = session.query(Product).filter(Product.name == self.name)
        return customerData


class Venta(Base):
    __tablename__ = 'venta'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    cantidad = Column(Integer)
    product = relationship("Product", back_populates="venta")


"""

from avances.gui.modelo.modelo import Base
import sqlalchemy as db
engine = db.create_engine('postgresql://rpython:rpython@localhost:5432/guipython', echo=True)
engine.connection = engine.connect()
Base.metadata.create_all(engine)
"""
