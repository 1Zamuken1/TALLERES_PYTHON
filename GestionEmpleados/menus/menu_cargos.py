"""
Menú para gestionar cargos y departamentos relacionados.
"""

from ..services.cargo_service import CargoService
from ..services.departamento_service import DepartamentoService
from ..validaciones.validaciones import validar_texto_no_vacio


def mostrar_menu_cargos():
    print("\n╔════════════════════════════════╗")
    print("║      GESTION DE CARGOS        ║")
    print("╠════════════════════════════════╣")
    print("║ 1. Listar cargos               ║")
    print("║ 2. Agregar cargo               ║")
    print("║ 3. Modificar cargo             ║")
    print("║ 4. Eliminar cargo              ║")
    print("║ 5. Gestionar departamentos     ║")
    print("║ 0. Regresar                    ║")
    print("╚════════════════════════════════╝")


def ejecutar_menu_departamentos():
    servicio_depto = DepartamentoService()
    while True:
        print("\n╔════════════════════════════════╗")
        print("║    GESTION DE DEPARTAMENTOS    ║")
        print("╠════════════════════════════════╣")
        print("║ 1. Listar departamentos        ║")
        print("║ 2. Agregar departamento        ║")
        print("║ 0. Regresar                    ║")
        print("╚════════════════════════════════╝")
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            servicio_depto.listar_departamentos()
        elif opcion == "2":
            servicio_depto.crear_departamento_interactivo()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")


def ejecutar_menu_cargos():
    servicio = CargoService()
    while True:
        mostrar_menu_cargos()
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            servicio.listar_cargos()
        elif opcion == "2":
            servicio.crear_cargo_interactivo()
        elif opcion == "3":
            codigo = validar_texto_no_vacio("Codigo del cargo a modificar: ").upper()
            servicio.modificar_cargo_interactivo(codigo)
        elif opcion == "4":
            codigo = validar_texto_no_vacio("Codigo del cargo a eliminar: ").upper()
            servicio.eliminar_cargo(codigo)
        elif opcion == "5":
            ejecutar_menu_departamentos()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")
