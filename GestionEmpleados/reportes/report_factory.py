"""
Fábrica simple para obtener estrategias de reporte.
Ilustra el patrón Factory junto con el patrón Strategy.
"""

from .reporte_txt_strategy import ReporteTXTStrategy


class ReportFactory:
    @staticmethod
    def obtener_estrategia(tipo="txt"):
        """Devuelve una instancia de estrategia según el tipo.

        Actualmente solo se soporta 'txt', pero se puede extender con
        nuevas clases (pdf, csv, etc.) sin modificar al cliente.
        """
        if tipo == "txt":
            return ReporteTXTStrategy()
        # en un escenario real lanzaríamos una excepción más explicativa
        raise ValueError(f"Tipo de reporte desconocido: {tipo}")
