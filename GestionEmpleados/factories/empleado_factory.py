"""
Patrón Factory para la creación de empleados.
Encapsula la lógica de instanciación/creación del estructura de datos del empleado.
"""

class EmpleadoFactory:
    """Fábrica para crear instancias de empleados (diccionarios en este caso)."""

    @staticmethod
    def crear_empleado(documento, nombre, celular, correo, codigo_cargo):
        """
        Crea un nuevo objeto empleado.
        
        Args:
            documento (str): Documento de identidad
            nombre (str): Nombre completo
            celular (str): Número de celular
            correo (str): Correo electrónico
            codigo_cargo (str): Código del cargo asignado
            
        Returns:
            dict: Estructura de datos del empleado
        """
        return {
            'documento': documento,
            'nombre': nombre,
            'celular': celular,
            'correo': correo,
            'cargo': codigo_cargo
        }
