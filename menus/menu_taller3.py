"""
Menú de Ejercicios del Taller 3
Agrupa los ejercicios de algoritmos básicos y estructuras de datos.
"""

def diseno_menu_ejercicios():
    """Muestra el diseño del menú de ejercicios"""
    print("╔════════════════════════════════════╗")
    print("║    TALLER 3 - EJERCICIOS           ║")
    print("╠════════════════════════════════════╣")
    print("║  1. Notas de Asignaturas           ║")
    print("║  2. Comisión de Vendedor           ║")
    print("║  3. Cesta de Compras               ║")
    print("║  4. Inventario Cloudata SAS        ║")
    print("╠════════════════════════════════════╣")
    print("║  0. Regresar al menú principal     ║")
    print("╚════════════════════════════════════╝")

def ejecutar_menu_taller3():
    """
    Controlador principal del menú de ejercicios.
    Permite seleccionar y ejecutar cada ejercicio del taller.
    """
    # Importaciones locales para evitar problemas de path
    import sys
    import os
    
    # Ruta a la carpeta 'ejercicios'
    ejercicios_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ejercicios'))
    
    # Agregar al path para importar módulos directamente
    if ejercicios_path not in sys.path:
        sys.path.insert(0, ejercicios_path)

    # También agregamos la carpeta raíz para importar como paquete si es necesario
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    
    try:
        # Intentamos importar directamente (si ejercicios_path está en sys.path)
        try:
            from materias import ejercicio_asignaturas
            from comision import ejercicio_comisiones
            from cesta_compras import ejercicio_cesta_compras
            from cloudata import ejecutar_cloudata
        except ImportError:
            # Fallback: intentar importar como paquete (si root_path está en sys.path)
            from ejercicios.materias import ejercicio_asignaturas
            from ejercicios.comision import ejercicio_comisiones
            from ejercicios.cesta_compras import ejercicio_cesta_compras
            from ejercicios.cloudata import ejecutar_cloudata
            
        # Diccionario de opciones
        menu_opciones = {
            "1": ejercicio_asignaturas,
            "2": ejercicio_comisiones,
            "3": ejercicio_cesta_compras,
            "4": ejecutar_cloudata,
        }
        
        while True:
            diseno_menu_ejercicios()
            try:
                opcion = input("Selecciona una opcion: ")
            except (KeyboardInterrupt, EOFError):
                print("\n╔════════════════════════════════════╗")
                print("║  Entrada cancelada, regresando...  ║")
                print("╚════════════════════════════════════╝")
                break
            
            if opcion == "0":
                print("╔════════════════════════════════════╗")
                print("║  Regresando al menú principal...   ║")
                print("╚════════════════════════════════════╝")
                break
            
            # Obtener función del diccionario
            funcion = menu_opciones.get(opcion)
            
            if funcion:
                try:
                    funcion()
                except Exception as e:
                    print(f"\n╔════════════════════════════════════╗")
                    print(f"║  Error al ejecutar ejercicio       ║")
                    print(f"║  {str(e)[:32]:32s}║")
                    print("╚════════════════════════════════════╝")
                input("\nPresiona Enter para continuar...")
            else:
                print("\nOpción no válida. Intenta de nuevo.")
                input("Presiona Enter para continuar...")
                
    except Exception as e:
        print(f"Error crítico importando módulos: {e}")
        input("Presiona Enter para volver...")
