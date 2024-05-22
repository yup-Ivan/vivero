from utiles.conectar import BaseDeDatos

class Semilla:

    def __init__(self, nombre, precio, stock):

        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def __str__(self):
        
        return f'Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}'

class Gestor:

    def __init__(self):
        self.db = BaseDeDatos()
        self.db.conectar()

    def __del__(self):
        self.db.desconectar()

    def nueva_semilla(self, semilla):
        self.db.lanzar(
            f"INSERT INTO semilla (nombre, precio, stock) VALUES ('{semilla.nombre}',{semilla.precio},{semilla.stock});"
            )

    def semillas(self):
        return self.db.lanzar(
            "SELECT * FROM semilla;"
        )

    def eliminacion_semilla(self, nombre):
        linea = (
            'DELETE FROM semilla WHERE nombre = %s;'
        )
        datos = (nombre,)
        self.db.lanzar(linea, datos)

    def actualizar_semilla(self, nombre, stock):
        linea = (
            'UPDATE semilla SET stock = stock + %s WHERE nombre = %s;'
        )
        datos = (stock, nombre)
        self.db.lanzar(linea, datos)

    def obtener_precio(self, nombre):
        linea = 'SELECT precio FROM semilla WHERE nombre = %s;'
        datos = (nombre,)
        precio = self.db.lanzar(linea, datos)
        return precio[0][0]
    
    def obtener_cantidad(self, nombre):
        linea = 'SELECT stock FROM semilla WHERE nombre = %s;'
        datos = (nombre,)
        stock = self.db.lanzar(linea, datos)
        return stock[0][0]
    
    def actualizar_carrito(self, nombre, cantidad):
        
        precio = self.obtener_precio(nombre)
        stock = self.obtener_cantidad(nombre)
        if cantidad > stock:
            return 'No tenemos suficiente stock.'
        linea = (
            'INSERT INTO carrito (nombre, precio, cantidad) VALUES (%s, %s, %s);'
        )
        datos = (nombre, precio, cantidad)
        self.db.lanzar(linea, datos)
        return f'Se han añadido semillas de: {nombre}, a {precio}$, {cantidad} uds.'

    def carrito(self):
        linea = (
            'SELECT * FROM carrito;'
        )
        return self.db.lanzar(linea,)

    def eliminar_carrito(self):
        linea = (
            'DELETE FROM carrito;'
        )    
        self.db.lanzar(linea,)    

    def comprar(self):
        lista_carrito = self.carrito()
        nombres = set()
        precio_final = 0
        for id, nombre, precio, cantidad in lista_carrito:
            nombres.add(nombre)
            precio_total = precio * cantidad
            precio_final += precio_total
        if precio_final > 0:
            return nombres, precio_final, True
        return nombres, precio_final, False

    def tablas(self):
        lineas = [
                """
                    CREATE TABLE if not exists semilla (
                        id int AUTO_INCREMENT,
                        nombre varchar (50),
                        precio float,
                        stock int,
                        PRIMARY KEY (id)
                    );
                """,
                """
                    CREATE TABLE if not exists carrito (
                        id int AUTO_INCREMENT,
                        nombre varchar (50),
                        precio float,
                        cantidad int,
                        PRIMARY KEY (id)
                    );                    
                """]
        for linea in lineas:
            self.db.lanzar(linea)