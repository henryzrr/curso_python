import sqlalchemy as db

engine = db.create_engine('postgresql://postgres:postgres@localhost:5432/prueba')
conexion = engine.connect()

