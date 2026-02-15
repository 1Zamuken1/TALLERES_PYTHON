"""
Módulo encargado de orquestar la creación de reportes utilizando
la estrategia definida en reporte_txt_strategy.
"""

from ..repositories.departamento_repository import DepartamentoRepository
from ..repositories.empleado_repository import EmpleadoRepository
from ..repositories.cargo_repository import CargoRepository
from .report_factory import ReportFactory


class GeneradorReportes:
    def __init__(self):
        self.depto_repo = DepartamentoRepository()
        self.empleado_repo = EmpleadoRepository()
        self.cargo_repo = CargoRepository()
        # la estrategia se obtiene a través de la fábrica
        self.strategy = ReportFactory.obtener_estrategia('txt')

    def reporte_departamento(self, codigo_departamento):
        dept = self.depto_repo.buscar_por_codigo(codigo_departamento)
        if not dept:
            return None
        empleados = self.empleado_repo.buscar_por_departamento(codigo_departamento)
        # enviar todos los cargos (la estrategia filtrará si es necesario)
        cargos_info = self.cargo_repo.obtener_todos()
        contenido = self.strategy.generar_reporte_departamento(dept, empleados, cargos_info)
        return self.strategy.guardar_archivo(contenido, nombre_base=f"reporte_{codigo_departamento}")

    def reporte_general(self):
        departamentos = self.depto_repo.obtener_todos().values()
        departamentos_data = []
        for dept in departamentos:
            empleados = self.empleado_repo.buscar_por_departamento(dept['codigo'])
            # todos los cargos (puede ser filtrado por depto en estrategia)
            cargos_info = self.cargo_repo.obtener_todos()
            departamentos_data.append((dept, empleados, cargos_info))
        contenido = self.strategy.generar_reporte_general(departamentos_data)
        return self.strategy.guardar_archivo(contenido, nombre_base="reporte_general")
