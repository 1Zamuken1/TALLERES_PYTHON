from .services import InventarioService

def validar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(">> Error: Ingrese un número entero válido.")

def validar_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(">> Error: Ingrese un valor numérico (ej: 1500.50).")

class ConsoleUI:
    def __init__(self):
        self.service = InventarioService()

    def iniciar(self):
        print("╔════════════════════════════════════════════╗")
        print("║      SISTEMA DE INVENTARIO CLOUDATA SAS    ║")
        print("╚════════════════════════════════════════════╝")

        n = validar_entero("¿Cuántos productos desea ingresar al inventario?: ")

        for i in range(n):
            self._registrar_producto(i + 1)

        self._mostrar_resumen_global()
        self._mostrar_menu()

    def _registrar_producto(self, indice):
        print(f"\n╔════ Registro del Producto #{indice} ═══════════════════╗")
        nombre = input("║ Nombre del producto: ")
        codigo = validar_entero("║ Código del producto: ")
        
        while True:
            tipo_prod = validar_entero("║ Tipo (1: Servicio, 2: Físico): ")
            if tipo_prod in [1, 2]: break
            print("║ >> Error: Seleccione 1 o 2.")

        while True:
            tipo_flete = validar_entero("║ Tipo de flete (1: Nacional, 2: Internacional): ")
            if tipo_flete in [1, 2]: break
            print("║ >> Error: Seleccione 1 o 2.")

        cantidad = validar_entero("║ Cantidad de producto: ")
        costo_sin_iva = validar_flotante("║ Precio costo (sin IVA): ")
        print("╚══════════════════════════════════════════════════╝")

        # Registrar y obtener el objeto modelo con los cálculos
        producto = self.service.registrar_producto(nombre, codigo, tipo_prod, tipo_flete, cantidad, costo_sin_iva)

        # Mostrar reporte individual
        print(f"\nResultados para {nombre}:")
        print(f" - Costo final por producto: {round(producto.calcular_costo_final_unitario(), 2)}")
        print(f" - Precio venta por producto: {round(producto.calcular_precio_venta_unitario(), 2)}")
        print(f" - Costo total (lote): {round(producto.calcular_costo_total_lote(), 2)}")
        print(f" - Valor ganancia por producto: {round(producto.calcular_valor_ganancia_unitario(), 2)}")

    def _mostrar_resumen_global(self):
        totales = self.service.obtener_resumen_global()
        print("\n╔════════════════════════════════════════════════╗")
        print("║      RESUMEN GENERAL DE INVENTARIO             ║")
        print("╠════════════════════════════════════════════════╣")
        print(f"╚══ Costo total (con fletes):       ${round(totales['total_costo'], 2):<14}")
        print(f"╚══ Ganancia total proyectada:      ${round(totales['total_ganancia'], 2):<14}")
        print(f"╚══ Valor total de fletes:          ${round(totales['total_fletes'], 2):<14}")
        print(f"╚══ Valor total de venta:           ${round(totales['total_venta'], 2):<14}")
        print(f"╚══ Costo total (sin fletes):       ${round(totales['total_costo_sin_flete'], 2):<14}")
        print("╚════════════════════════════════════════════════╝")

    def _mostrar_menu(self):
        while True:
            print("\n╔════════════════════════════════════════════════╗")
            print("║            MENÚ DE CONSULTA                    ║")
            print("╠════════════════════════════════════════════════╣")
            print("║ 1) Mostrar costo total de los productos        ║")
            print("║ 2) Mostrar total de ganancia de los productos  ║")
            print("║ 3) Mostrar valor total de venta de productos   ║")
            print("║ 4) Salir del sistema                           ║")
            print("║ 5) Abrir Interfaz Gráfica                      ║")
            print("╚════════════════════════════════════════════════╝")
            
            opcion = input("Seleccione una tarea: ")
            totales = self.service.obtener_resumen_global()

            if opcion == "1":
                print(f"\n>> El COSTO TOTAL (incluye flete e IVA) es: ${round(totales['total_costo'], 2)}")
            elif opcion == "2":
                print(f"\n>> La GANANCIA TOTAL es: ${round(totales['total_ganancia'], 2)}")
            elif opcion == "3":
                print(f"\n>> El VALOR TOTAL DE VENTA es: ${round(totales['total_venta'], 2)}")
            elif opcion == "4":
                print("Saliendo del sistema de Cloudata SAS...")
                break
            elif opcion == "5":
                self._abrir_gui()
            else:
                print("Opción no válida.")
    
    def _abrir_gui(self):
        """Abre la interfaz gráfica de Cloudata"""
        try:
            from .gui import CloudataGUI
            print("\n>> Abriendo interfaz gráfica...")
            app = CloudataGUI(service=self.service)
            app.ejecutar()
            print("\n>> Interfaz gráfica cerrada. Regresando al menú de consola...")
        except Exception as e:
            print(f"\n>> Error al abrir la interfaz gráfica: {str(e)}")

