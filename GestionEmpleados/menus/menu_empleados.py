"""
Menú de gestión de empleados. Cada opción invoca al
EmpleadoService para realizar las operaciones.
"""

from ..services.empleado_service import EmpleadoService
from ..validaciones.validaciones import validar_documento


def mostrar_menu_empleados():
    print("\n╔════════════════════════════════╗")
    print("║     GESTION DE EMPLEADOS       ║")
    print("╠════════════════════════════════╣")
    print("║ 1. Listar empleados            ║")
    print("║ 2. Agregar empleado            ║")
    print("║ 3. Modificar empleado          ║")
    print("║ 4. Eliminar empleado           ║")
    print("║ 5. Buscar empleado             ║")
    print("║ 0. Regresar                    ║")
    print("╚════════════════════════════════╝")


def ejecutar_menu_empleados():
    servicio = EmpleadoService()
    while True:
        mostrar_menu_empleados()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            servicio.listar_empleados()
        elif opcion == "2":
            servicio.crear_empleado_interactivo()
        elif opcion == "3":
            doc = validar_documento("Documento del empleado a modificar: ")
            servicio.modificar_empleado_interactivo(doc)
        elif opcion == "4":
            doc = validar_documento("Documento del empleado a eliminar: ")
            servicio.eliminar_empleado(doc)
        elif opcion == "5":
            doc = validar_documento("Documento del empleado a buscar: ")
            servicio.buscar_empleado(doc)
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presiona Enter para continuar...")
