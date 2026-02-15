"""
Menú para generación de reportes por departamento o general.
"""

from ..reportes.generador_reportes import GeneradorReportes
from ..validaciones.validaciones import validar_texto_no_vacio


def mostrar_menu_reportes():
    print("\n╔════════════════════════════════╗")
    print("║       GENERAR REPORTES         ║")
    print("╠════════════════════════════════╣")
    print("║ 1. Reporte por departamento    ║")
    print("║ 2. Reporte general             ║")
    print("║ 0. Regresar                    ║")
    print("╚════════════════════════════════╝")


def ejecutar_menu_reportes():
    generador = GeneradorReportes()
    while True:
        mostrar_menu_reportes()
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            codigo = validar_texto_no_vacio("Codigo del departamento: ").upper()
            ruta = generador.reporte_departamento(codigo)
            if ruta:
                print(f"Reporte creado en {ruta}")
            else:
                print("No se pudo generar el reporte. Revise el codigo del departamento.")
        elif opcion == "2":
            ruta = generador.reporte_general()
            if ruta:
                print(f"Reporte general creado en {ruta}")
            else:
                print("No se pudo generar el reporte general.")
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")
