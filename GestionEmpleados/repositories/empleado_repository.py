"""
Repositorio de Empleados
Patron Repository para acceso a datos

P. Repository -> Encapsula la lógica de acceso a datos proporcionando
una interfaz similar a una colección para acceder a los objetos del dominio.
"""

from ..database.db_singleton import BaseDatos

class EmpleadoRepository:
    """
    Repositorio para CRUD de empleados
    """
    
    def __init__(self):
        """
        Inicializa el repositorio con la instancia de la BD
        
        Usamos P. Singleton para siempre obtener la misma instancia
        """
        self.db = BaseDatos()
        self.db.inicializar()
        
    def agregar(self, empleado):
        """
        Agregar nuevo empleado
        
        Args:
            empleado (dict): Diccionario con datos del empleado:
                {
                   'documento': str,
                    'nombre': str,
                    'celular': str,
                    'correo': str,
                    'cargo': str (codigo del cargo) 
                }
        Returns:
            bool: True si se agregó exitosamente
        """
        documento = empleado['documento']
        self.db.empleados[documento] = empleado
        self.db.guardar_en_archivo()
        return True
    
    def buscar_por_documento(self, documento):
        """
        Buscar un empleado por su documento.
        
        Args:
            documento (str): Numero de documento
        Returns:
            dict: Diccionario del empleado si existe
            None: Si no existe
        """
        return self.db.empleados.get(documento)
    
    def modificar(self, documento, empleado_actualizado):
        """
        Modifica los datos de un empleado existente

        Args:
            documento (str): Documento del empleado a modificar
            empleado_actualizado (dict): Nuevos datos
        """
        if documento in self.db.empleados:
            self.db.empleados[documento] = empleado_actualizado
            self.db.guardar_en_archivo()
            return True
        return False
    
    def eliminar(self, documento):
        """
        Elimina un empleado de la BD

        Args:
            documento (str): Documento del empleado
        Return:
            bool: True si se eliminó, False si no existe
        """
        if documento in self.db.empleados:
            del self.db.empleados[documento]
            self.db.guardar_en_archivo()
            return True
        return False
    
    def obtener_todos(self):
        """
        Obtiene todos los empleados.
        
        Returns:
            dict: Diccionario con todos los empleados {documento: datos}
        """
        return self.db.empleados
    
    def buscar_por_cargo(self, codigo_cargo):
        """
        Busca todos los empleados que tienen unc argo específico.

        Args:
            codigo_cargo (str): Código del cargo
        Returns:
            list: Lista de diccionarios de empleados con ese cargo
        """
        empleados_cargo = []
        for empleado in self.db.empleados.values():
            if empleado['cargo'] == codigo_cargo:
                empleados_cargo.append(empleado)
        return empleados_cargo
    
    def buscar_por_departamento(self, codigo_departamento):
        """
        Busca todos los empleados de un departamento.
        
        Primero obtiene los cargos del departamento, luego busca
        empleados que tengan esos cargos.

        Args:
            codigo_departamento (str): Código del departamento
        Returns:
            list: Lista de diccionarios de empleados del departamento
        """
        # Obtener todos los cargos del departamento
        cargos_depto = []
        for cargo in self.db.cargos.values():
            if cargo['departamento'] == codigo_departamento:
                cargos_depto.append(cargo['codigo'])
        
        # Buscar empleados con esos cargos
        empleados_depto = []
        for empleado in self.db.empleados.values():
            if empleado['cargo'] in cargos_depto:
                empleados_depto.append(empleado)
        return empleados_depto
    
    def existe_documento(self, documento):
        """
        Verifica si ya existe un empleado con ese documento

        Args:
            documento (str): Documento a verificar
        Returns:
            bool: True si existe, False si no
        """
        return documento in self.db.empleados
