"""
Repositorio de Cargos
Contiene operaciones CRUD para cargos dentro de la BD Singleton.
"""

from ..database.db_singleton import BaseDatos


class CargoRepository:
    """Repositorio para cargos de la empresa."""

    def __init__(self):
        self.db = BaseDatos()
        # inicializar provoca carga de archivo si existe
        self.db.inicializar()

    def agregar(self, cargo):
        """Agrega un cargo nuevo.

        Args:
            cargo (dict): {'codigo': str, 'nombre': str, 'departamento': str}
        Returns:
            bool: True si se agregó
        """
        codigo = cargo['codigo']
        self.db.cargos[codigo] = cargo
        # persistir
        self.db.guardar_en_archivo()
        return True

    def buscar_por_codigo(self, codigo):
        return self.db.cargos.get(codigo)

    def modificar(self, codigo, cargo_actualizado):
        if codigo in self.db.cargos:
            self.db.cargos[codigo] = cargo_actualizado
            self.db.guardar_en_archivo()
            return True
        return False

    def eliminar(self, codigo):
        if codigo in self.db.cargos:
            del self.db.cargos[codigo]
            self.db.guardar_en_archivo()
            return True
        return False

    def obtener_todos(self):
        return self.db.cargos

    def existe_codigo(self, codigo):
        return codigo in self.db.cargos

    def buscar_por_departamento(self, codigo_departamento):
        return [c for c in self.db.cargos.values() if c.get('departamento') == codigo_departamento]
