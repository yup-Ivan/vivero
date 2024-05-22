def f_nueva_semilla(continuar=True):        
    while continuar:
        try:
            nombre_semilla = input('Introduce el nombre de la nueva semilla: ')
            precio_semilla = float(input('Introduce el precio del sobre de semillas: '))
            stock_semilla = int(input('Introduce el stock de semillas: '))
            continuar = False
            return nombre_semilla, precio_semilla, stock_semilla
        except:
            print('Introduciste algo mal, recuerda precio es float y stock int.')

def f_eliminar_semilla(continuar=True):
    while continuar:
        try:
            nombre = input('Introduce el nombre de la semilla a eliminar: ')
            if nombre:
                return nombre
        except:
            print('Hay algo mal, intenta de nuevo.')

def f_actualizar_semilla(continuar=True):
    while continuar:
        try:
            nombre = input('Introduce el nombre de la semilla a actualizar: ')
            stock = int(input('Introduce stock a sumar: '))
            if nombre and stock > 0:
                return nombre, stock
        except:
            print('Hay algo mal, intenta de nuevo.')

def f_agregar_semilla_carrito(continuar=True):
    while continuar:
        try:
            nombre = input('Introduce el nombre de la semilla a comprar: ')
            cantidad = int(input('Introduce cantidad a comprar: '))
            if nombre and cantidad > 0:
                return nombre, cantidad
        except:
            print('Hay algo mal, intenta de nuevo.')

if __name__ == '__main__':
    nombre_semilla, precio_semilla, stock_semilla = f_nueva_semilla()
    print(nombre_semilla, precio_semilla, stock_semilla)