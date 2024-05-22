from utiles.funciones import Gestor
from utiles.formularios import (f_nueva_semilla, 
                                f_eliminar_semilla,
                                f_actualizar_semilla,
                                f_agregar_semilla_carrito,
                                )
from utiles.objetos import Semilla

def menu_principal():
    return ("""
    //-------------------//
    1. Nueva semilla.
    2. Ver semillas.
    3. Eliminar semilla.
    4. Actualizar stock.
    //-------------------//
    5. Añadir carrito.
    6. Ver carrito.
    7. Comprar.
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

            nombre_semilla_eliminar = f_eliminar_semilla()
            gestionar.eliminacion_semilla(nombre_semilla_eliminar)
        
        elif opcion_principal == '4':

            nombre_semilla_actualizar, nuevo_stock = f_actualizar_semilla()
            gestionar.actualizar_semilla(nombre_semilla_actualizar, nuevo_stock)

        elif opcion_principal == '5':

            nombre_semilla, cantidad = f_agregar_semilla_carrito()
            resp = gestionar.actualizar_carrito(nombre_semilla, cantidad)
            print(resp)

        elif opcion_principal == '6':

            lista_carrito = gestionar.carrito()
            
            print(f"\nTU CARRITO DE LA COMPRA\n{'ID':<10}{'Nombre':<10}{'Precio':<10}{'Cantidad':<10}")
            for id, nombre, precio, cantidad in lista_carrito:
                print(f'{id:<10}{nombre:<10}{precio:<10}{cantidad:<10}')
        
        elif opcion_principal == '7':

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