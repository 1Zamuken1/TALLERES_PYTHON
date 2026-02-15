"""
Base de Datos Singleton
Implementa el patrón Singleton para garantizar una única instancia y
proporciona un punto de acceso global a la Base de datos.

Cómo funciona?:
- Primera vez: Crea la instancia y la guarda
- Siguientes veces: Retorna la instancia existente
"""

import json
import os

class BaseDatos:
    """
    Clase que mantiene la BD en memoria
    
    Estructura de datos:
    - departamentos: {codigo: {datos}}
    - cargos: {codigo: {datos}}
    - empleados: {documento: {datos}}
    """
    
    _instancia = None
    
    def __new__(cls):
        """
        Implementación de Singleton
        
        Este método se llama antes de __init__ y controla la creación de instancias
        Si la instancia ya existe; entonces la retorna
        
        Returns:
            BaseDatos: la única instancia de la clase
        """
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia
    
    def inicializar(self):
        """
        Inicializa la BD con datos precargados.
        solo se ejecuta 1 vez debido al  flag _inicializado.

        Antes de poblar valores por defecto intenta cargar la
        información desde un archivo JSON. Si éste existe la
        base de datos en memoria se sustituye por el contenido del
        archivo y no se reutilizan los datos de ejemplo.

        Departamentos:
        - DEP001: RH
        - DEP002: Vicepresidencia Técnica
        - DEP003: Ventas
        """

        if self._inicializado:
            return

        # Primero intentar cargar datos persistidos
        if self.cargar_desde_archivo():
            # la carga establece _inicializado internamente
            return

        # Diccionario de departamentos
        self.departamentos = {
            "DEP001": {
                "codigo": "DEP001",
                "nombre": "Recursos Humanos"
            },
            "DEP002": {
                "codigo": "DEP002",
                "nombre": "Vicepresidencia Técnica"
            },
            "DEP003": {
                "codigo": "DEP003",
                "nombre": "Ventas"
            }
        }
        
        # Diccionario de cargos
        self.cargos = {
            # RH - DEP001
            "CAR001": {
                "codigo": "CAR001",
                "nombre": "Gerente de RH",
                "departamento": "DEP001"
            },
            "CAR002": {
                "codigo": "CAR002",
                "nombre": "Analista de Seleccion",
                "departamento": "DEP001"
            },
            "CAR003": {
                "codigo": "CAR003",
                "nombre": "Coordinador de Nomina",
                "departamento": "DEP001"
            },
            "CAR004": {
                "codigo": "CAR004",
                "nombre": "Especialista en Capacitacion",
                "departamento": "DEP001"
            },
            "CAR005": {
                "codigo": "CAR005",
                "nombre": "Asistente de RH",
                "departamento": "DEP001"
            },
            
            # Vicepresidencia Técnica - DEP002
            "CAR006": {
                "codigo": "CAR006",
                "nombre": "Vicepresidente Tecnico",
                "departamento": "DEP002"
            },
            "CAR007": {
                "codigo": "CAR007",
                "nombre": "Arquitecto de Software",
                "departamento": "DEP002"
            },
            "CAR008": {
                "codigo": "CAR008",
                "nombre": "Desarrollador Senior",
                "departamento": "DEP002"
            },
            "CAR009": {
                "codigo": "CAR009",
                "nombre": "Analista de Sistemas",
                "departamento": "DEP002"
            },
            "CAR010": {
                "codigo": "CAR010",
                "nombre": "Ingeniero DevOps",
                "departamento": "DEP002"
            },
            
            # Ventas - DEP003
            "CAR011": {
                "codigo": "CAR011",
                "nombre": "Gerente de Ventas",
                "departamento": "DEP003"
            },
            "CAR012": {
                "codigo": "CAR012",
                "nombre": "Ejecutivo de Cuentas",
                "departamento": "DEP003"
            },
            "CAR013": {
                "codigo": "CAR013",
                "nombre": "Analista de Mercadeo",
                "departamento": "DEP003"
            },
            "CAR014": {
                "codigo": "CAR014",
                "nombre": "Representante Comercial",
                "departamento": "DEP003"
            },
            "CAR015": {
                "codigo": "CAR015",
                "nombre": "Coordinador de Ventas",
                "departamento": "DEP003"
            }
        }
        
        # Diccionario de empleados
        self.empleados = {
            "1001": {
                "documento": "1001",
                "nombre": "juan perez",
                "celular": "3001234567",
                "correo": "juan.perez@empresa.com",
                "cargo": "CAR001" # Gerente de RH
            },
            "1002": {
                "documento": "1002",
                "nombre": "ana garcia",
                "celular": "3007654321",
                "correo": "ana.garcia@empresa.com",
                "cargo": "CAR002"  # Analista de Seleccion
            },
            "1003": {
                "documento": "1003",
                "nombre": "carlos lopez",
                "celular": "3009876543",
                "correo": "carlos.lopez@empresa.com",
                "cargo": "CAR006"  # Vicepresidente Tecnico
            },
            "1004": {
                "documento": "1004",
                "nombre": "maria rodriguez",
                "celular": "3005551234",
                "correo": "maria.rodriguez@empresa.com",
                "cargo": "CAR008"  # Desarrollador Senior
            },
            "1005": {
                "documento": "1005",
                "nombre": "pedro sanchez",
                "celular": "3005559876",
                "correo": "pedro.sanchez@empresa.com",
                "cargo": "CAR011"  # Gerente de Ventas
            }
        }
        
        self._inicializado = True
        
    def guardar_en_archivo(self, ruta="database/datos.json"):
        """
        Guarda toda la BD en un archivo JSON.
        
        Los diccionarios al convertirse perfectamente en JSON
        permiten que los datos persistan entre ejecuciones
        
        Args:
            ruta (str): Ruta del archivo donde guardar
            
        Returns:
            bool: True si ha guardado de forma exitosa
        """
        try:
            datos_completos = {
                "departamentos": self.departamentos,
                "cargos": self.cargos,
                "empleados": self.empleados
            }
            
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(ruta), exist_ok = True)
            
            with open(ruta, 'w', encoding='utf-8') as archivo:
                json.dump(datos_completos, archivo, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False
        
    def cargar_desde_archivo(self, ruta="database/datos.json"):
        """
        Carga la BD desde un archivo JSON
        
        Args:
            ruta (str): Ruta del archivo a cargar
        
        Returns:
            bool: True si se cargó exitosamente
        """
        try:
            if not os.path.exists(ruta):
                return False
            with open(ruta, 'r', encoding='utf-8') as archivo:
                datos_completos = json.load(archivo)
        except Exception as e:
            print(f"Error al cargar: {e}")
            return False
        
        # si llegamos acá es porque el archivo fue leído correctamente
        # y los datos contienen las tres tablas esperadas
        self.departamentos = datos_completos.get("departamentos", {})
        self.cargos = datos_completos.get("cargos", {})
        self.empleados = datos_completos.get("empleados", {})
        self._inicializado = True
        return True