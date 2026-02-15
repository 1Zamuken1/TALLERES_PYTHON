"""
Menu Principal del Sistema de Gestion de Empleados
Todos los menus usan diseño manual con caracteres especiales.
"""

from .menu_empleados import ejecutar_menu_empleados
from .menu_cargos import ejecutar_menu_cargos
from .menu_reportes import ejecutar_menu_reportes


def mostrar_menu_principal():
    """Muestra el menu principal (diseño manual)."""
    print("╔══════════════════════════════════════╗")
    print("║   GESTION DE EMPLEADOS               ║")
    print("╠══════════════════════════════════════╣")
    print("║  1. Gestion de Empleados             ║")
    print("║  2. Gestion de Cargos                ║")
    print("║  3. Generar Reportes                 ║")
    print("╠══════════════════════════════════════╣")
    print("║  0. Salir                            ║")
    print("╚══════════════════════════════════════╝")


def ejecutar_menu_principal():
    """
    Controlador del menu principal.
    
    Permite acceder a las diferentes funcionalidades del sistema.
    """
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            ejecutar_menu_empleados()
        elif opcion == "2":
            ejecutar_menu_cargos()
        elif opcion == "3":
            ejecutar_menu_reportes()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presiona Enter para continuar...")