"""
Reporte TXT
P. Strategy para generar reportes en formato de txt

El P. Strategy define una familia de algoritmos, encapsula cada uno
y los hace intercambiables.
Strategy permite que el algoritmo varíe independientemente de los
clientes que lo usan.
"""

from tabulate import tabulate
from datetime import datetime
import os

class ReporteTXTStrategy:
    """
    Estrategia para generar reportes con tablas formateadas
    """
    
    def generar_reporte_departamento(self, departamento, empleados, cargos_info):
        """
        Genera un reporte completo de un departamento

        Args:
            departamento (dict): Datos del departamento
            empleados (list): Lista de empleados del departamento
            cargos_info (dict): Diccionario de cargos {codigo: datos}
        Returns:
            str: Contenido del reporte en formato txt
        """
    def generar_reporte_departamento(self, departamento, empleados, cargos_info):
        """
        Genera un reporte completo de un departamento
        
        Args:
            departamento (dict): Datos del departamento
            empleados (list): Lista de empleados del departamento
            cargos_info (dict): Diccionario de cargos {codigo: datos}
        Returns:
            str: Contenido del reporte en formato txt
        """
        contenido = ""
        
        # Encabezado
        contenido += "="*80 + "\n"
        contenido += f"REPORTE DE DEPARTAMENTO: {departamento['nombre'].upper()}\n"
        contenido += f"Codigo: {departamento['codigo']}\n"
        contenido += f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        contenido += "="*80 + "\n"
        contenido += "\n"
        
        # Tabla de empleados
        if empleados:
            datos_tabla = []
            for emp in empleados:
                cargo = cargos_info.get(emp['cargo'], {})
                datos_tabla.append([
                    emp['documento'],
                    emp['nombre'].title(),
                    cargo.get('nombre', 'N/A'),
                    emp['celular'],
                    emp['correo']
                ])
            
            headers = ["Documento", "Nombre", "Cargo", "Celular", "Correo"]
            tabla = tabulate(datos_tabla, headers=headers, tablefmt="grid")
            contenido += tabla + "\n"
        else:
            contenido += "No hay empleados en este departamento.\n"
        
        contenido += "\n"
        contenido += f"Total de empleados: {len(empleados)}\n"
        contenido += "="*80 + "\n"
        
        return contenido
    
    def generar_reporte_general(self, departamentos_data):
        """
        Genera un reporte general de toda la empresa.
        
        Args:
            departamentos_data (list): Lista de tuplas (departamento, empleados, cargos)
        
        Returns:
            str: Contenido del reporte completo
        """
    def generar_reporte_general(self, departamentos_data):
        """
        Genera un reporte general de toda la empresa.
        
        Args:
            departamentos_data (list): Lista de tuplas (departamento, empleados, cargos)
        
        Returns:
            str: Contenido del reporte completo
        """
        contenido = ""
        
        # Encabezado general
        contenido += "="*80 + "\n"
        contenido += "REPORTE GENERAL DE LA EMPRESA\n"
        contenido += f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        contenido += "="*80 + "\n"
        contenido += "\n"
        
        total_empleados = 0
        
        # Reporte por cada departamento
        contador = 0
        for departamento, empleados, cargos_info in departamentos_data:
            if contador > 0:
                contenido += "\n\n"
            contador += 1
            
            contenido += "-"*80 + "\n"
            contenido += f"DEPARTAMENTO: {departamento['nombre'].upper()}\n"
            contenido += "-"*80 + "\n"
            contenido += "\n"
            
            if empleados:
                datos_tabla = []
                for emp in empleados:
                    cargo = cargos_info.get(emp['cargo'], {})
                    datos_tabla.append([
                        emp['documento'],
                        emp['nombre'].title(),
                        cargo.get('nombre', 'N/A'),
                        emp['celular'],
                        emp['correo']
                    ])
                
                headers = ["Documento", "Nombre", "Cargo", "Celular", "Correo"]
                tabla = tabulate(datos_tabla, headers=headers, tablefmt="grid")
                contenido += tabla + "\n"
                contenido += "\n"
                contenido += f"Subtotal: {len(empleados)} empleado(s)\n"
                total_empleados += len(empleados)
            else:
                contenido += "No hay empleados en este departamento.\n"
                contenido += "\n"
        
        # Resumen final
        contenido += "\n"
        contenido += "="*80 + "\n"
        contenido += "RESUMEN GENERAL\n"
        contenido += "="*80 + "\n"
        contenido += f"Total de departamentos: {len(departamentos_data)}\n"
        contenido += f"Total de empleados: {total_empleados}\n"
        contenido += "="*80 + "\n"
        
        return contenido
    
    def guardar_archivo(self, contenido, nombre_base="reporte"):
        """
        Guarda el reporte en un archivo TXT.
        
        Args:
            contenido (str): Contenido del reporte
            nombre_base (str): Nombre base del archivo
        
        Returns:
            str: Ruta del archivo guardado, o None si fallo
        """
        try:
            # Crear carpeta reportes si no existe
            os.makedirs("reportes", exist_ok=True)
            
            # Nombre con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"reportes/{nombre_base}_{timestamp}.txt"
            
            # Guardar
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)
            
            return nombre_archivo
        except Exception as e:
            print(f"Error al guardar archivo: {e}")
            return None