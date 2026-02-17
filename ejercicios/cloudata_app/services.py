from .models import Producto
from .repositories import ProductoRepository

class InventarioService:
    def __init__(self):
        self.repository = ProductoRepository()

    def registrar_producto(self, nombre, codigo, tipo_producto, tipo_flete, cantidad, costo_sin_iva):
        nuevo_producto = Producto(
            nombre=nombre,
            codigo=codigo,
            tipo_producto=tipo_producto,
            tipo_flete=tipo_flete,
            cantidad=cantidad,
            costo_sin_iva=costo_sin_iva
        )
        self.repository.agregar(nuevo_producto)
        return nuevo_producto

    def obtener_todos_productos(self):
        """Obtiene todos los productos del inventario"""
        return self.repository.obtener_todos()

    def obtener_resumen_global(self):
        productos = self.repository.obtener_todos()
        
        total_costo = 0
        total_ganancia = 0
        total_fletes = 0
        total_venta = 0
        total_costo_sin_flete = 0

        for p in productos:
            total_costo += p.calcular_costo_total_lote()
            total_ganancia += p.calcular_ganancia_total_lote()
            total_fletes += p.calcular_flete_total_lote()
            total_venta += p.calcular_venta_total_lote()
            total_costo_sin_flete += p.calcular_costo_sin_flete_lote()

        return {
            "total_costo": total_costo,
            "total_ganancia": total_ganancia,
            "total_fletes": total_fletes,
            "total_venta": total_venta,
            "total_costo_sin_flete": total_costo_sin_flete
        }
