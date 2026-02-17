"""
Punto de entrada para el Sistema de Inventario Cloudata SAS.
Permite seleccionar entre interfaz de consola o gráfica.
"""

from cloudata_app.ui import ConsoleUI
from cloudata_app.gui import CloudataGUI

def ejecutar_cloudata():
    """Muestra menú de selección de modo y lanza la interfaz elegida"""
    print("\n╔════════════════════════════════════════════════╗")
    print("║   SISTEMA DE INVENTARIO CLOUDATA SAS           ║")
    print("╠════════════════════════════════════════════════╣")
    print("║  Seleccione el modo de ejecución:              ║")
    print("║                                                ║")
    print("║  1) Interfaz de Consola                        ║")
    print("║  2) Interfaz Gráfica (Tkinter)                 ║")
    print("║                                                ║")
    print("║  0) Regresar                                   ║")
    print("╚════════════════════════════════════════════════╝")
    
    while True:
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            # Modo consola
            ConsoleUI().iniciar()
            break
        elif opcion == "2":
            # Modo gráfico
            try:
                print("\n>> Abriendo interfaz gráfica...")
                app = CloudataGUI()
                app.ejecutar()
                print("\n>> Interfaz gráfica cerrada.")
            except Exception as e:
                print(f"\n>> Error al abrir la interfaz gráfica: {str(e)}")
            break
        elif opcion == "0":
            print("╔════════════════════════════════════════════════╗")
            print("║  Regresando al menú anterior...                ║")
            print("╚════════════════════════════════════════════════╝")
            break
        else:
            print(">> Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_cloudata()
