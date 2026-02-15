"""
Servicio para manejar departamentos de manera interactiva.
"""

from ..repositories.departamento_repository import DepartamentoRepository
from ..validaciones.validaciones import validar_texto_no_vacio


class DepartamentoService:
    def __init__(self):
        self.depto_repo = DepartamentoRepository()

    def crear_departamento_interactivo(self):
        print("╔════════════════════════════════╗")
        print("║   AGREGAR NUEVO DEPARTAMENTO   ║")
        print("╚════════════════════════════════╝")

        while True:
            codigo = validar_texto_no_vacio("Codigo del departamento: ").upper()
            if self.depto_repo.existe_codigo(codigo):
                print("Error: ese código ya existe.")
            else:
                break
        nombre = validar_texto_no_vacio("Nombre del departamento: ").title()
        departamento = {"codigo": codigo, "nombre": nombre}
        self.depto_repo.agregar(departamento)
        print("Departamento agregado.")
        input("Presione Enter para continuar...")
        return departamento

    def listar_departamentos(self):
        deps = self.depto_repo.obtener_todos()
        if not deps:
            print("No hay departamentos registrados.")
            return []
        from tabulate import tabulate
        datos = [[d['codigo'], d['nombre']] for d in deps.values()]
        print(tabulate(datos, headers=["Codigo", "Nombre"], tablefmt="grid"))
        input("\nPresione Enter para continuar...")
        return list(deps.values())
