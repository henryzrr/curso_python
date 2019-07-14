import sqlite3
conn=sqlite3.connect('ejemplo.db')
c=conn.cursor()

c.execute('''CREATE TABLE prueba(hola text)''')
conn.commit()
conn.close()

