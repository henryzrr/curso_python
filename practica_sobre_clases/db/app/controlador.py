from modelos import *
from sqlalchemy.orm import Session

#### Trabajadores###
def add_trabajador(ci,nombre,edad):
    dataBase = DataBase()
    session = Session(bind=dataBase.conexion)
    t = Trabajador(ci=ci,nombre=nombre,anhos=edad)
    session.add(t)
    session.commit()

def del_trabajador(ci):
    pass
def get_trabajadores():
    pass
def update_trabajadores(ci,*args):
    pass

###Proyectos###
def add_proyecto(id_proyecto,nombre_proyecto):
    pass
def del_proyecto(id):
    pass
def get_proyectos():
    pass
def update_proyectos(id,*args):
    pass
###Cargo###
def add_cargo(id_cargo,nombre_cargo,salario):
    pass
def del_cargo(id):
    pass
def get_cargos():
    pass
def update_cargo(id,*args):
    pass
###Contrato###
def add_contrato(id_contrato,empleado,proyecto,cargo):
    pass
def del_contrato(id):
    pass
def get_contratos():
    pass
def update_contrato(id,*args):
    pass