"""
Sistema de Gestion de Hotel - Punto de Entrada Principal

Este es el archivo principal que ejecuta el sistema de gestion hotelera.
Proporciona el menu principal para acceder a las funcionalidades del sistema.

Funcionalidades principales:
- Realizar nuevas reservaciones
- Login para clientes y administradores
- Gestion completa de reservas
- Generacion de informes

Uso:
    python main.py

Autor: Sistema de Gestion Hotelera
Version: 1.0.0
"""

from reservas import crear_reservacion
from autenticacion import sistema_login


def limpiar_pantalla():
    """
    Imprime lineas vacias para simular limpieza de pantalla.
    
    En un sistema real, se podria usar os.system('clear') en Linux/Mac
    o os.system('cls') en Windows, pero para mantener compatibilidad
    y simplicidad, usamos este enfoque.
    
    Returns:
        None
    """
    print("\n" * 2)


def mostrar_menu_principal():
    """
    Muestra el menu principal del sistema.
    
    Esta funcion solo imprime el menu, no maneja la logica de seleccion.
    Aplica el principio Single Responsibility.
    
    Returns:
        None
    """
    print("\n=======================================")
    print("SISTEMA DE GESTION DE HOTEL")
    print("=======================================")
    print("1. Realizar nueva reservacion")
    print("2. Ingresar al sistema (Login)")
    print("3. Salir")
    print("=======================================")


def sistema_hotel_main():
    """
    Funcion principal del sistema de gestion de hotel.
    
    Este es el punto de entrada principal que controla el flujo del programa.
    Presenta un menu con tres opciones:
    
    1. Realizar nueva reservacion:
       - Permite a nuevos clientes crear una reserva
       - Captura datos personales, fechas, tipo de habitacion
       - Asigna habitacion disponible
       - Genera codigo de ticket unico
       
    2. Ingresar al sistema (Login):
       - Para clientes: ver/modificar/cancelar su reserva
       - Para admin: ver todas las reservas y generar informes
       
    3. Salir:
       - Cierra el sistema
    
    El sistema mantiene un ciclo infinito hasta que el usuario
    seleccione la opcion de salir.
    
    Principios SOLID aplicados:
    - Single Responsibility: Solo controla el flujo principal
    - Dependency Inversion: Delega operaciones a modulos especializados
    - Open/Closed: Facil agregar nuevas opciones al menu
    
    Returns:
        None
    
    Example:
        >>> sistema_hotel_main()
        =======================================
        SISTEMA DE GESTION DE HOTEL
        =======================================
        1. Realizar nueva reservacion
        2. Ingresar al sistema (Login)
        3. Salir
        =======================================
        Seleccione una opcion: 1
    """
    print("Bienvenido al Sistema de Gestion de Hotel")
    print("Desarrollado para automatizar procesos hoteleros")
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            # Crear nueva reservacion
            limpiar_pantalla()
            crear_reservacion()
            
        elif opcion == "2":
            # Sistema de login
            limpiar_pantalla()
            sistema_login()
            
        elif opcion == "3":
            # Salir del sistema
            print("\n=======================================")
            print("Gracias por usar nuestro sistema")
            print("Hasta pronto!")
            print("=======================================")
            break
            
        else:
            print("\nOpcion no valida. Por favor seleccione 1, 2 o 3.")
            input("Presiona Enter para continuar...")


# Punto de entrada del programa
# Este bloque solo se ejecuta si el archivo es ejecutado directamente
# No se ejecuta si el archivo es importado como modulo
if __name__ == "__main__":
    sistema_hotel_main()
