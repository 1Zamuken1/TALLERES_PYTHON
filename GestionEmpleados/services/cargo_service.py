"""
Servicio para la lógica de negocio relacionada con cargos.
"""

from ..repositories.cargo_repository import CargoRepository
from ..repositories.departamento_repository import DepartamentoRepository
from ..validaciones.validaciones import validar_texto_no_vacio


class CargoService:
    def __init__(self):
        self.cargo_repo = CargoRepository()
        self.depto_repo = DepartamentoRepository()

    def crear_cargo_interactivo(self):
        print("╔════════════════════════════════╗")
        print("║      AGREGAR NUEVO CARGO      ║")
        print("╚════════════════════════════════╝")

        # código único
        while True:
            codigo = validar_texto_no_vacio("Codigo del cargo: ").upper()
            existe = self.cargo_repo.existe_codigo(codigo)
            if existe == True:
                print("Error: ese código ya existe.")
            else:
                break

        nombre = validar_texto_no_vacio("Nombre del cargo: ")
        nombre = nombre.title()

        # elegir departamento
        print("Departamentos disponibles:")
        deptos = self.depto_repo.obtener_todos()
        for cod, dept in deptos.items():
            print(f"  {cod} - {dept['nombre']}")
        
        while True:
            codigo_depto = validar_texto_no_vacio("Codigo de departamento: ").upper()
            existe_dep = self.depto_repo.existe_codigo(codigo_depto)
            if existe_dep == True:
                break
            print("Error: departamento inválido.")

        cargo = {}
        cargo["codigo"] = codigo
        cargo["nombre"] = nombre
        cargo["departamento"] = codigo_depto
        
        self.cargo_repo.agregar(cargo)
        print("Cargo creado exitosamente.")
        input("Presione Enter para continuar...")
        return cargo

    def modificar_cargo_interactivo(self, codigo):
        cargo = self.cargo_repo.buscar_por_codigo(codigo)
        if not cargo:
            print("Cargo no encontrado.")
            return False

        print("╔════════════════════════════════╗")
        print("║      MODIFICAR CARGO          ║")
        print("╚════════════════════════════════╝")
        print(f"Cargo actual: {cargo['nombre']}")
        print("Deje en blanco para mantener el valor actual")

        nombre_input = input(f"Nombre [{cargo['nombre']}]: ").strip()
        nombre = nombre_input.title() if nombre_input else cargo['nombre']

        print("Departamentos disponibles:")
        for cod, dept in self.depto_repo.obtener_todos().items():
            print(f"  {cod} - {dept['nombre']}")
        dept_input = input(f"Departamento [{cargo['departamento']}]: ").strip().upper()
        departamento = dept_input if dept_input else cargo['departamento']
        if departamento and not self.depto_repo.existe_codigo(departamento):
            print("Departamento inválido, se mantendrá el original.")
            departamento = cargo['departamento']

        cargo_actualizado = {
            "codigo": codigo,
            "nombre": nombre,
            "departamento": departamento
        }
        if self.cargo_repo.modificar(codigo, cargo_actualizado):
            print("Cargo modificado.")
            input("Presione Enter para continuar...")
            return True
        print("Error al modificar cargo.")
        return False

    def eliminar_cargo(self, codigo):
        if self.cargo_repo.eliminar(codigo):
            print("Cargo eliminado exitosamente.")
            input("Presione Enter para continuar...")
            return True
        print("Cargo no encontrado o no se pudo eliminar.")
        return False

    def listar_cargos(self):
        cargos = self.cargo_repo.obtener_todos()
        if not cargos:
            print("No hay cargos registrados.")
            return []
        datos = []
        for c in cargos.values():
            dept = self.depto_repo.buscar_por_codigo(c['departamento'])
            datos.append([c['codigo'], c['nombre'], dept['nombre'] if dept else 'N/A'])
        from tabulate import tabulate
        print(tabulate(datos, headers=["Codigo", "Nombre", "Departamento"], tablefmt="grid"))
        input("\nPresione Enter para continuar...")
        return list(cargos.values())
