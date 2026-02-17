class Producto:
    def __init__(self, nombre, codigo, tipo_producto, tipo_flete, cantidad, costo_sin_iva):
        self.nombre = nombre
        self.codigo = codigo
        self.tipo_producto = tipo_producto  # 1: Servicio, 2: Físico
        self.tipo_flete = tipo_flete        # 1: Nacional, 2: Internacional
        self.cantidad = cantidad
        self.costo_sin_iva = costo_sin_iva

    def calcular_valor_flete(self):
        # Si el tipo de flete a aplicar es nacional (1) se debe aplicar el 20%
        # Si el tipo de flete a aplicar es internacional (2) se debe aplicar el 45%
        porcentaje_flete = 20 if self.tipo_flete == 1 else 45
        return self.costo_sin_iva * percentage_flete / 100

    def calcular_valor_flete_unitario(self):
         # Corrección: El cálculo del enunciado dice:
         # valorFlete = costoSinIvaPorProducto * porcentajeFlete / 100
         porcentaje = 20 if self.tipo_flete == 1 else 45
         return self.costo_sin_iva * porcentaje / 100

    def calcular_costo_final_unitario(self):
        # formulaIva = 1 + (porcentajeIva / 100) -> 1.19
        # costoFinalPorProducto = (costoSinIvaPorProducto * 1.19) + valorFlete
        factor_iva = 1.19
        valor_flete = self.calcular_valor_flete_unitario()
        return (self.costo_sin_iva * factor_iva) + valor_flete

    def calcular_valor_ganancia_unitario(self):
        # Si es servicio (1) -> 20%, Si es físico (2) -> 35%
        # valorGananciaPorProducto = costoSinIvaPorProducto * porcentajeGanacia / 100
        porcentaje = 20 if self.tipo_producto == 1 else 35
        return self.costo_sin_iva * porcentaje / 100

    def calcular_precio_venta_unitario(self):
        # precioVentaPorProducto = costoFinalProducto + valorGananciaPorProducto
        # NOTA: costoFinalProducto aqui se refiere al unitario calculado anteriormente
        return self.calcular_costo_final_unitario() + self.calcular_valor_ganancia_unitario()

    # Totales del lote
    def calcular_costo_total_lote(self):
        return self.calcular_costo_final_unitario() * self.cantidad

    def calcular_ganancia_total_lote(self):
        return self.calcular_valor_ganancia_unitario() * self.cantidad

    def calcular_flete_total_lote(self):
        return self.calcular_valor_flete_unitario() * self.cantidad

    def calcular_venta_total_lote(self):
        return self.calcular_precio_venta_unitario() * self.cantidad
    
    def calcular_costo_sin_flete_lote(self):
        # Costo total de los productos sin incluir el valor del flete (solo con IVA)
        factor_iva = 1.19
        costo_unitario_con_iva_sin_flete = self.costo_sin_iva * factor_iva
        return costo_unitario_con_iva_sin_flete * self.cantidad
