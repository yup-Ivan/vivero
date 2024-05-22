import mysql.connector
from mysql.connector import Error

class BaseDeDatos:

    def __init__(self):
        self.conexion = None
        self.config = {
            'host' : 'localhost',
            'port' : '3310',
            'user' : 'vivero',
            'password' : 'vivero',
            'database' : 'vivero_db'
        }

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.config)
            if self.conexion.is_connected():
                return self.conexion
        except:
            print('001: Error al conectar con la base de datos.')

    def desconectar(self):
        try:
            if self.conexion.is_connected():
                self.conexion.close()
            else:
                print('No estas conectado.')
        except:
            print('001: Error al conectar con la base de datos.')

    def lanzar(self, linea, datos=None):
        try:
            if self.conexion.is_connected():
                with self.conexion.cursor() as cursor:
                    cursor.execute(linea, datos)
                    if cursor.description:
                        return cursor.fetchall()
                    self.conexion.commit()
                    return
        except Error as e:
            print('Error al lanzar una sentencia: ', e)


if __name__ == '__main__':
    db = BaseDeDatos()
    db.conectar()