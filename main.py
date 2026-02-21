"""
Sistema de Talleres Python - Menu Principal
Punto de entrada principal del sistema de talleres.

Este archivo implementa el super menu que permite acceder a todos
los talleres disponibles. Cada taller tiene su propio modulo en
la carpeta 'menus/', siguiendo el principio Single Responsibility.

Principios SOLID aplicados:
- Single Responsibility: Este archivo solo maneja el menu principal
- Open/Closed: Facil agregar nuevos talleres sin modificar este archivo
- Dependency Inversion: Importa menus sin conocer su implementacion interna

Uso:
    python main.py

Estructura del proyecto:
    main.py                 # Menu principal (este archivo)
    menus/
        __init__.py
        menu_taller1.py     # Taller 1 - Variables
        menu_taller2_banco.py   # Taller 2 - Cuenta Bancaria
        menu_taller2_ciclos.py  # Taller 2 - Ciclo For y While
    Taller1_Ref/            # Ejercicios del Taller 1
    cuenta_bancaria/        # Ejercicios de cuenta bancaria
    Taller2_while_for/      # Ejercicios de ciclos

Autor: Sistema de Talleres Python
Version: 2.0.0
"""

from menus.menu_taller1 import ejecutar_menu_taller_1
from menus.menu_taller2_banco import ejecutar_menu_taller_2_banco
from menus.menu_taller2_ciclos import ejecutar_menu_taller_2_ciclos
from menus.menu_taller3 import ejecutar_menu_taller3
from Hotel.Ejercicio22 import ejercicio_sistema_hotel
from GestionEmpleados.main import sistema_gestion_empleados
from proyecto.proyecto_datetime import ejercicio_gestion_proyecto


def diseno_menu_principal():
    """
    Imprime la interfaz visual del menu principal en ASCII.
    
    Muestra los talleres disponibles:
    - Taller 1: Variables
    - Taller 2: Cuenta Bancaria
    - Taller 2: Ciclo For y While (22 ejercicios)
    
    Returns:
        None
    """
    print("╔════════════════════════════════════╗")
    print("║    TALLERES PYTHON                 ║")
    print("╠════════════════════════════════════╣")
    print("║  1. Taller 1 - Variables           ║")
    print("║  2. Taller 2 - Cuenta Bancaria     ║")
    print("║  3. Taller 2 - Ciclo for y While   ║")
    print("║  4. Ejercicio Hotel                ║")
    print("║  5. Gestión de Empleados           ║")
    print("║  6. Taller 3 - Ejercicios          ║")
    print("║  7. Gestión de Proyecto            ║")
    print("╠════════════════════════════════════╣")
    print("║  0. Salir                          ║")
    print("╚════════════════════════════════════╝")


def ejecutar_menu_principal():
    """
    Controlador logico del menu principal.
    
    Implementa el punto de entrada principal del sistema que:
    1. Muestra el menu de talleres disponibles
    2. Captura la opcion del usuario
    3. Ejecuta el menu del taller seleccionado
    4. Maneja opciones invalidas
    5. Permite salir del programa (opcion "0")
    
    Cada taller esta modularizado en su propio archivo dentro de la
    carpeta 'menus/', lo que facilita el mantenimiento y escalabilidad
    del sistema.
    
    El uso de un diccionario para mapear opciones a funciones aplica
    el principio Open/Closed: es facil agregar nuevos talleres sin
    modificar la logica de este controlador.
    
    Returns:
        None
    """
    # Diccionario que mapea opciones a funciones de menus de talleres
    menu_talleres = {
        "1": ejecutar_menu_taller_1,
        "2": ejecutar_menu_taller_2_banco,
        "3": ejecutar_menu_taller_2_ciclos,
        "4": ejercicio_sistema_hotel,
        "5": sistema_gestion_empleados,
        "6": ejecutar_menu_taller3,
        "7": ejercicio_gestion_proyecto,
    }
    
    # Mensaje de bienvenida (estética uniforme)
    print("╔════════════════════════════════════╗")
    print("║    BIENVENIDO AL SISTEMA           ║")
    print("╚════════════════════════════════════╝")
    
    while True:
        diseno_menu_principal()
        try:
            opcion = input("Selecciona una opcion: ")
        except (KeyboardInterrupt, EOFError):
            # Ctrl+C o fin de entrada, rompemos el bucle con mensaje suave
            print("\n╔════════════════════════════════════╗")
            print("║  Entrada cancelada, saliendo...    ║")
            print("╚════════════════════════════════════╝")
            break

        if opcion == "0":
            print("╔════════════════════════════════════╗")
            print("║  Gracias por usar el sistema       ║")
            print("║  Hasta pronto!                     ║")
            print("╚════════════════════════════════════╝")
            break

        # Obtener funcion del diccionario
        opcion_menu = menu_talleres.get(opcion)

        if opcion_menu:
            # Llamar a la funcion del taller seleccionado
            opcion_menu()
        else:
            print("\nOpcion no valida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")


# Punto de entrada del programa
# Este bloque solo se ejecuta si el archivo es ejecutado directamente
# No se ejecuta si el archivo es importado como modulo
if __name__ == "__main__":
    ejecutar_menu_principal()
