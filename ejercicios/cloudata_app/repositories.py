import json
import os
from .models import Producto

class ProductoRepository:
    # Guardar el archivo JSON en la misma carpeta que este script (cloudata_app/)
    ARCHIVO_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "productos.json")

    def __init__(self):
        # Al iniciar, cargamos los datos del archivo si existe
        self.productos = self._cargar_datos()

    def agregar(self, producto):
        self.productos.append(producto)
        self._guardar_datos()
        return producto

    def obtener_todos(self):
        return self.productos

    def _guardar_datos(self):
        """Guarda la lista de productos en el archivo JSON"""
        datos = []
        for p in self.productos:
            datos.append({
                "nombre": p.nombre,
                "codigo": p.codigo,
                "tipo_producto": p.tipo_producto,
                "tipo_flete": p.tipo_flete,
                "cantidad": p.cantidad,
                "costo_sin_iva": p.costo_sin_iva
            })
        
        try:
            with open(self.ARCHIVO_DB, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4)
        except Exception as e:
            print(f"Error guardando datos: {e}")

    def _cargar_datos(self):
        """Carga los productos desde el archivo JSON"""
        if not os.path.exists(self.ARCHIVO_DB):
            return []
        
        try:
            with open(self.ARCHIVO_DB, "r", encoding="utf-8") as f:
                datos = json.load(f)
                productos = []
                for d in datos:
                    prod = Producto(
                        d["nombre"],
                        d["codigo"],
                        d["tipo_producto"],
                        d["tipo_flete"],
                        d["cantidad"],
                        d["costo_sin_iva"]
                    )
                    productos.append(prod)
                return productos
        except Exception as e:
            print(f"Error cargando datos: {e}")
            return []
