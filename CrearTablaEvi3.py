import sqlite3
from sqlite3 import Error
import sys

try:
    with sqlite3.connect("Ventas.db") as conn:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS venta ( \
                    clave INTEGER PRIMARY KEY, \
                    fecha TEXT);""")

        c.execute("""CREATE TABLE IF NOT EXISTS articulos ( \
                    descripcion TEXT, \
                    piezas INTEGER, \
                    precio REAL, \
                    clave INTEGER, \
                    FOREIGN KEY (clave) REFERENCES venta (clave)   );""")

        print("Tabla creada exitosamente")
except Error as e:
    print (e)
except Exception:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")