"""
Menu del Taller 1 - Variables
Gestiona la navegacion y ejecucion de ejercicios del primer taller.

Principio SOLID aplicado:
- Single Responsibility: Solo maneja la logica del Taller 1
- Dependency Inversion: Importa funciones sin conocer su implementacion
"""

from Taller1_Ref.Ejercicio1 import ejercicio_suma_edades
from Taller1_Ref.Ejercicio2 import promedio_temperaturas
from Taller1_Ref.Ejercicio3 import dividir_litros_agua
from Taller1_Ref.Ejercicio4 import ejercicio_comprar_gaseosa
from Taller1_Ref.Ejercicio5 import kilometros_caminados
from Taller1_Ref.Ejercicio6 import convertir_grados_C_a_F
from Taller1_Ref.Ejercicio7 import compra_tres_alimentos
from Taller1_Ref.Ejercicio8 import dividir_dulces
from Taller1_Ref.Ejercicio9 import calcular_imc
from Taller1_Ref.Ejercicio10 import dividir_cuenta


def diseno_menu_taller_1():
    """
    Imprime la interfaz visual del menu del Taller 1 en ASCII.
    
    Muestra las 10 opciones de ejercicios disponibles y la opcion
    para regresar al menu principal.
    
    Returns:
        None
    """
    print("╔════════════════════════════════════╗")
    print("║     TALLER 1 - VARIABLES           ║")
    print("╠════════════════════════════════════╣")
    print("║  1. Suma de edades                 ║")
    print("║  2. Promedio de temperaturas       ║")
    print("║  3. Division de agua               ║")
    print("║  4. Calculo de cambio              ║")
    print("║  5. Kilometros caminados           ║")
    print("║  6. Conversion Celsius-Fahrenheit  ║")
    print("║  7. Total de compra                ║")
    print("║  8. Division de dulces             ║")
    print("║  9. Calculo de IMC                 ║")
    print("║ 10. Division de cuenta             ║")
    print("╠════════════════════════════════════╣")
    print("║  0. Regresar                       ║")
    print("╚════════════════════════════════════╝")


def ejecutar_menu_taller_1():
    """
    Controlador logico que administra el acceso a los ejercicios del Taller 1.
    
    Implementa un ciclo infinito que:
    1. Muestra el menu
    2. Captura la opcion del usuario
    3. Ejecuta el ejercicio correspondiente
    4. Maneja opciones invalidas
    5. Permite regresar al menu principal (opcion "0")
    
    Usa un diccionario para mapear opciones a funciones, aplicando
    el principio Open/Closed: facil agregar ejercicios sin modificar
    la logica del controlador.
    
    Returns:
        None
    
    Example:
        >>> ejecutar_menu_taller_1()
        [Muestra menu]
        Selecciona una opcion: 1
        [Ejecuta ejercicio_suma_edades]
    """
    # Diccionario que mapea opciones a funciones de ejercicios
    menu_ejercicios = {
        "1": ejercicio_suma_edades,
        "2": promedio_temperaturas,
        "3": dividir_litros_agua,
        "4": ejercicio_comprar_gaseosa,
        "5": kilometros_caminados,
        "6": convertir_grados_C_a_F,
        "7": compra_tres_alimentos,
        "8": dividir_dulces,
        "9": calcular_imc,
        "10": dividir_cuenta,
    }

    while True:
        diseno_menu_taller_1()
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "0":
            print("Regresando al menu principal...")
            break
        
        # Obtener funcion del diccionario
        # .get devuelve None si la opcion no existe
        opcion_menu = menu_ejercicios.get(opcion)
        
        if opcion_menu:
            # Llamar a la funcion correspondiente
            opcion_menu()
        else:
            print("Opcion no valida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")
