"""
Repositorio de Departamentos
Permite acceder y modificar la tabla de departamentos.
"""

from ..database.db_singleton import BaseDatos


class DepartamentoRepository:
    """CRUD básico para departamentos."""

    def __init__(self):
        self.db = BaseDatos()
        self.db.inicializar()

    def obtener_todos(self):
        return self.db.departamentos

    def buscar_por_codigo(self, codigo):
        return self.db.departamentos.get(codigo)

    def agregar(self, departamento):
        codigo = departamento['codigo']
        self.db.departamentos[codigo] = departamento
        self.db.guardar_en_archivo()
        return True

    def existe_codigo(self, codigo):
        return codigo in self.db.departamentos

    def modificar(self, codigo, departamento_actualizado):
        if codigo in self.db.departamentos:
            self.db.departamentos[codigo] = departamento_actualizado
            self.db.guardar_en_archivo()
            return True
        return False

    def eliminar(self, codigo):
        if codigo in self.db.departamentos:
            del self.db.departamentos[codigo]
            self.db.guardar_en_archivo()
            return True
        return False
