from utiles.models import (Gestor, 
                           Semilla)
from utiles.formularios import (f_nueva_semilla, 
                                f_nombre_semilla,
                                f_actualizar_semilla,
                                f_agregar_semilla_carrito,)

def menu_principal():
    return ("""
    //-------------------//
    1. Nueva semilla.
    2. Ver semillas.
    3. Eliminar semilla.
    4. Actualizar stock.
    5. Ver precio de una semilla.
    6. Ver stock de una semilla.
    //-------------------//
    7. Añadir carrito.
    8. Ver carrito.
    9. Comprar.
    //-------------------//
    0. Salir.
    //-------------------//
    """)

def empezar_gestion(gestionando=True):

    gestionar = Gestor()
    gestionar.tablas()
    
    while gestionando:

        print(menu_principal())

        opcion_principal = input()
        
        if opcion_principal == '1':

            nombre_semilla, precio_semilla, stock_semilla = f_nueva_semilla()
            semilla = Semilla(nombre_semilla, precio_semilla, stock_semilla)
            gestionar.nueva_semilla(semilla)

        elif opcion_principal == '2':

            lista_semillas = gestionar.semillas()
            print(f"\nLISTA SEMILLAS\n{'ID':<10}{'Nombre':<10}{'Precio':<10}{'Stock':<10}")
            for id, nombre, precio, stock in lista_semillas:
                print(f"{id:<10}{nombre:<10}{precio:<10}{stock:<10}")

        elif opcion_principal == '3':

            nombre_semilla_eliminar = f_nombre_semilla('eliminar')
            gestionar.eliminacion_semilla(nombre_semilla_eliminar)
        
        elif opcion_principal == '4':

            nombre_semilla_actualizar, nuevo_stock = f_actualizar_semilla()
            gestionar.actualizar_semilla(nombre_semilla_actualizar, nuevo_stock)

        elif opcion_principal == '5':

            nombre = f_nombre_semilla('precio')
            precio = gestionar.obtener_precio(nombre)
            print(f'El precio de la semilla: {nombre}, es {precio}$ / ud.')

        elif opcion_principal == '6': 

            nombre = f_nombre_semilla('stock')
            stock = gestionar.obtener_cantidad(nombre)
            print(f'El stock de la semilla: {nombre}, es de: {stock} uds.')

        elif opcion_principal == '7':

            nombre_semilla, cantidad = f_agregar_semilla_carrito()
            resp = gestionar.actualizar_carrito(nombre_semilla, cantidad)
            print(resp)

        elif opcion_principal == '8':

            lista_carrito = gestionar.carrito()
            
            print(f"\nTU CARRITO DE LA COMPRA\n{'ID':<10}{'Nombre':<10}{'Precio':<10}{'Cantidad':<10}")
            for id, nombre, precio, cantidad in lista_carrito:
                print(f'{id:<10}{nombre:<10}{precio:<10}{cantidad:<10}')
        
        elif opcion_principal == '9':

            nombres, precio_final, ok = gestionar.comprar()
            if ok:
                print(f'\nFACTURA FINAL: \nPrecio final: {precio_final}$.')
                for i, nombre in enumerate(nombres, 1):
                    print(f"Semilla: {i}, {nombre}.")
                print('\nGracias por comprar.')
                gestionar.eliminar_carrito()
                gestionando = False
            else:
                print('No puedes comprar 0 semillas.')

        elif opcion_principal == '0':

            print('Gracias por usar vivero online.')
            gestionando = False

        else:

            print('Te has equivocado de opción.')
    
empezar_gestion()