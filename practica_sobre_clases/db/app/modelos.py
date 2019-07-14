from database import DataBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey

Base = declarative_base()

class Trabajador(Base):
    __tablename__='trabajador'

    ci = Column(Integer,primary_key=True)
    nombre = Column(String)
    anhos = Column(Integer)

class Proyecto(Base):
    __tablename__='proyecto'
    id_proyecto = Column(Integer,primary_key=True)
    nombre_proyecto = Column(String)

class Cargo(Base):
    __tablename__='cargo'
    id_cargo = Column(Integer,primary_key=True)
    nombre_cargo = Column(String)
    salario=Column(Integer)

class contrato(Base):
    __tablename__='contrato'
    id_contrato = Column(Integer,primary_key=True)
    id_cargo = Column(Integer,ForeignKey('cargo.id_cargo'))
    id_proyecto = Column(Integer,ForeignKey('proyecto.id_proyecto'))
    empleado_ci=Column(Integer,ForeignKey('trabajador.ci'))

def crear_database():
    db=DataBase()
    Base.metadata.create_all(db.engine)

#crear_database()