from .database.db_singleton import BaseDatos
from .menus.menu_empleados import mostrar_menu_empleados, ejecutar_menu_empleados
from .menus.menu_cargos import mostrar_menu_cargos, ejecutar_menu_cargos
from .menus.menu_reportes import mostrar_menu_reportes, ejecutar_menu_reportes

def sistema_gestion_empleados():
    """
    Función principal del módulo de Gestión de Empleados.
    Se invoca desde el menú principal de Talleres_Python.
    """
    # Inicializar Base de Datos (Singleton)
    db = BaseDatos()
    db.inicializar()

    print("\nBienvenido al Sistema de Gestión de Recursos Humanos")
    print("Seleccione la interfaz que desea utilizar:")
    print("1. Consola (Texto)")
    print("2. Gráfica (Ventana)")
    
    opcion = input("Opción: ")
    
    if opcion == '2':
        iniciar_gui()
    else:
        iniciar_consola()

def iniciar_gui():
    try:
        from .gui.main_window import MainWindow
        app = MainWindow()
        app.mainloop()
        print("Cerrando interfaz gráfica...")
    except ImportError as e:
        print(f"Error al cargar la interfaz gráfica: {e}")
        print("Asegúrese de tener Tkinter instalado.")

def iniciar_consola():
    while True:
        print("\n╔══════════════════════════════════════╗")
        print("║   GESTION DE EMPLEADOS               ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Gestion de Empleados             ║")
        print("║  2. Gestion de Cargos                ║")
        print("║  3. Generar Reportes                 ║")
        print("╠══════════════════════════════════════╣")
        print("║  0. Salir                            ║")
        print("╚══════════════════════════════════════╝")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            while True:
                mostrar_menu_empleados()
                if not ejecutar_menu_empleados():
                    break
        elif opcion == "2":
            while True:
                mostrar_menu_cargos()
                if not ejecutar_menu_cargos():
                    break
        elif opcion == "3":
            while True:
                mostrar_menu_reportes()
                if not ejecutar_menu_reportes():
                    break
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida.")