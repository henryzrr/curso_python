import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
engine = db.create_engine('sqlite:///prueba.db')
conexion = engine.connect()

base = declarative_base()

class User(base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    def __repr__(self):
        return "<User(nombre='%s')>" % (self.name)

class Materia(base):
    __tablename__='materia'

    id_materia = db.Column(db.Integer,primary_key=True)
    nombre_materia = db.Column(db.String)

    def __init__(self,nombre):
        self.nombre_materia=nombre

base.metadata.create_all(engine)
m = Materia("hola")
session  = Session(bind=engine)
session.add(m)
session.commit()
print(m.nombre_materia)