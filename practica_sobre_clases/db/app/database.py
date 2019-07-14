from sqlalchemy import create_engine

class DataBase():
    def __init__(self):
        self.engine = create_engine('sqlite:///base.db')
        self.conexion =self.engine.connect()