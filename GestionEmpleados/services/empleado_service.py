"""
Servicio de Empleados
Cntiene la lógica de negocio para gestión de empleados

P. Service Layer
"""

from ..repositories.empleado_repository import EmpleadoRepository
from ..repositories.cargo_repository import CargoRepository
from ..factories.empleado_factory import EmpleadoFactory
from ..validaciones.validaciones import(
    validar_texto_no_vacio,
    validar_documento,
    validar_celular,
    validar_correo,
    confirmar_accion
)

class EmpleadoService:
    """
    Servicio que maneja la lógica del negocio de empleados
    """
    
    def __init__(self):
        """
        Inicializa el servicio con sus dependencias
        """
        self.empleado_repo = EmpleadoRepository()
        self.cargo_repo = CargoRepository()
    
    def crear_empleado_interactivo(self):
        """
        Crea un empleado de forma interactiva pidiendo datos al usuario
        
        Returns:
            dict: Empleado creado, o Nino si se canceló
        """
        
        print("╔════════════════════════════════════╗")
        print("║      AGREGAR NUEVO EMPLEADO        ║")
        print("╚════════════════════════════════════╝")
        
        # Validar documento único
        while True:
            documento = validar_documento("Documento: ")
            existe = self.empleado_repo.existe_documento(documento)
            if existe == True:
                print("Error: ya existe un empleado con ese documento.")
                continuar = input("Desea intentar con otro documento? (si/no): ").lower()
                if continuar != 'si':
                    return None
            else:
                break
            
        # Solicitar datos
        nombre = validar_texto_no_vacio("Nombre completo: ").lower()
        celular = validar_celular("Celular (10 dígitos): ")
        correo = validar_correo("Correo electrónico: ")
        
        # Mostrar cargos disponibles
        print("╔════════════════════════════════╗")
        print("║      Cargos disponibles:       ║")
        print("╚════════════════════════════════╝")
        cargos_dict = self.cargo_repo.obtener_todos()
        for codigo, cargo in cargos_dict.items():
            print(f"╚══ {codigo} - {cargo['nombre']}")
            
        while True:
            codigo_cargo = validar_texto_no_vacio("Codigo del cargo: ").upper()
            existe_cargo = self.cargo_repo.existe_codigo(codigo_cargo)
            if existe_cargo == True:
                break
            print("Error: Código de cargo inválido.")
        
        # Usar Factory para crear el empleado
        nuevo_emp = EmpleadoFactory.crear_empleado(
            documento=documento,
            nombre=nombre,
            celular=celular,
            correo=correo,
            codigo_cargo=codigo_cargo
        )

        # Guardar
        guardado = self.empleado_repo.agregar(nuevo_emp)
        if guardado == True:
            print("Empleado agregado exitosamente!")
            input("Presione Enter para continuar...")
            return nuevo_emp
        else:
            print("Error al agregar empleado.")
            return None
        
    def modificar_empleado_interactivo(self, documento):
        """
        Modifica un empleado existente.

        Args:
            documento (str): Documento del empleado
        Returns:
            bool: True si se modificó
        """
        emp_actual = self.empleado_repo.buscar_por_documento(documento)
        if emp_actual is None:
            print("Error: Empleado no encontrado.")
            return False
        
        print("╔════════════════════════════════╗")
        print("║      MODIFICAR EMPLEADO        ║")
        print("╚════════════════════════════════╝")
        print(f"Empleado actual: {emp_actual['nombre'].title()}")
        print("Deje en blanco para mantener el valor actual")
        
        # Solicitar nuevos datos (opcional)
        nombre_in = input(f"Nombre [{emp_actual['nombre']}]: ").strip().lower()
        if nombre_in:
            nombre = nombre_in
        else:
            nombre = emp_actual['nombre']
        
        celular_in = input(f"Celular [{emp_actual['celular']}]: ").strip()
        if celular_in:
            celular = celular_in
        else:
            celular = emp_actual['celular']
        
        correo_in = input(f"Correo [{emp_actual['correo']}]: ").strip().lower()
        if correo_in:
            correo = correo_in
        else:
            correo = emp_actual['correo']
        
        # Mostrar cargo actual y opciones
        cargo_actual = self.cargo_repo.buscar_por_codigo(emp_actual['cargo'])
        print(f"\nCargo actual: {cargo_actual['nombre']}")
        cambiar_cargo = input("Desea cambiar el cargo? (si/no): ").lower()
        
        codigo_cargo = emp_actual['cargo']
        if cambiar_cargo == 'si':
            print("\nCargos disponibles:")
            todos_cargos = self.cargo_repo.obtener_todos()
            for codigo, cargo in todos_cargos.items():
                print(f"  {codigo} - {cargo['nombre']}")
            
            while True:
                codigo_cargo = validar_texto_no_vacio("\nCodigo del cargo: ").upper()
                existe = self.cargo_repo.existe_codigo(codigo_cargo)
                if existe == True:
                    break
                print("Error: Codigo de cargo invalido.")
                
        # Actualizar usando Factory para mantener consistencia structure
        emp_upd = EmpleadoFactory.crear_empleado(
            documento=documento,
            nombre=nombre,
            celular=celular,
            correo=correo,
            codigo_cargo=codigo_cargo
        )
        
        modificado = self.empleado_repo.modificar(documento, emp_upd)
        if modificado == True:
            print("Empleado modificado exitosamente!")
            input("Presione Enter para continuar...")
            return True
        else:
            print("Error al modificar empleado.")
            return False
        
    def eliminar_empleado(self, documento):
        """
        Elimina un empleado.
        
        Args:
            documento (str): Documento del empleado
        
        Returns:
            bool: True si se elimino
        """
        emp = self.empleado_repo.buscar_por_documento(documento)
        if emp is None:
            print("Error: Empleado no encontrado.")
            return False
        
        print(f"Empleado: {emp['nombre'].title()}")
        confirmacion = confirmar_accion("Esta seguro que desea eliminar este empleado? (si/no): ")
        if confirmacion == True:
            eliminado = self.empleado_repo.eliminar(documento)
            if eliminado == True:
                print("Empleado eliminado exitosamente.")
                input("Presione Enter para continuar...")
                return True
        
        print("Operacion cancelada.")
        return False
    
    def listar_empleados(self):
        """
        Lista todos los empleados con formato tabla.
        
        Returns:
            list: Lista de empleados con informacion completa
        """
        from tabulate import tabulate
        
        empleados = self.empleado_repo.obtener_todos()
        
        if not empleados:
            print("No hay empleados registrados.")
            return []
        
        # Preparar datos para la tabla
        datos_tabla = []
        for emp in empleados.values():
            cargo = self.cargo_repo.buscar_por_codigo(emp['cargo'])
            datos_tabla.append([
                emp['documento'],
                emp['nombre'].title(),
                cargo['nombre'] if cargo else 'N/A',
                emp['celular'],
                emp['correo']
            ])
        
        # Ordenar por nombre
        datos_tabla.sort(key=lambda x: x[1])
        
        headers = ["Documento", "Nombre", "Cargo", "Celular", "Correo"]
        tabla = tabulate(datos_tabla, headers=headers, tablefmt="grid")
        
        print("╔════════════════════════════════╗")
        print("║      LISTA DE EMPLEADOS:       ║")
        print("╚════════════════════════════════╝")
        print(tabla)
        print(f"Total: {len(empleados)} empleado(s)")
        input("\nPresione Enter para continuar...")
        
        return list(empleados.values())
    
    def buscar_empleado(self, documento):
        """
        busca y muestra un empleado

        Args:
            documento (str): Documento del empleado
        Returns:
            dict: Empleado encontrado, o None
        """
        from tabulate import tabulate
        
        empleado = self.empleado_repo.buscar_por_documento(documento)
        
        if not empleado:
            print("Empleado no encontrado.")
            return None
        
        cargo = self.cargo_repo.buscar_por_codigo(empleado['cargo'])
        
        datos = [
            ["Documento", empleado['documento']],
            ["Nombre", empleado['nombre'].title()],
            ["Celular", empleado['celular']],
            ["Correo", empleado['correo']],
            ["Cargo", cargo['nombre'] if cargo else 'N/A']
        ]
        
        tabla = tabulate(datos, tablefmt="grid")
        print("╔════════════════════════════════╗")
        print("║   INFORMACIÓN DEL EMPLEADO     ║")
        print("╚════════════════════════════════╝")
        print(tabla)
        input("\nPresione Enter para continuar...")
        
        return empleado
