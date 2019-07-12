import sqlalchemy as db

class Database:

    def __init__(self):
        # self.engine = db.create_engine('postgresql://rpython:rpython@localhost:5432/guipython')
        self.engine = db.create_engine('postgresql://postgres:postgres@localhost:5432/prueba')
        self.connection = self.engine.connect()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance
