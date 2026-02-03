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

def diseno_menu():
    """
    Imprime la interfáz visual del menú en ASCII
    """
    print("╔════════════════════════════════════╗")
    print("║     TALLER PYTHON - VARIABLES      ║")
    print("╠════════════════════════════════════╣")
    print("║  1. Suma de edades                 ║")
    print("║  2. Promedio de temperaturas       ║")
    print("║  3. División de agua               ║")
    print("║  4. Cálculo de cambio              ║")
    print("║  5. Kilómetros caminados           ║")
    print("║  6. Conversión Celsius-Fahrenheit  ║")
    print("║  7. Total de compra                ║")
    print("║  8. División de dulces             ║")
    print("║  9. Cálculo de IMC                 ║")
    print("║ 10. División de cuenta             ║")
    print("╠════════════════════════════════════╣")
    print("║  0. Salir                          ║")
    print("╚════════════════════════════════════╝")
    
def ejecutar_menu_taller_1():
    """ 
    Controlador lógico que administra el acceso a los ejercicios del Taller 1 en base a las entradas del usuario.
    En caso de Ejecutar una opción no existente o letra; el programa regresará al menú al detectar una opción no válida.
    Si el usuario ingresa "0", el programa finalizará su ejecución.
    """
    
    # Diccionario que permita acceder a los ejercicios
    # Refactorizado para evitar crear nuevas opciones en match más adelante
    
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
        diseno_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "0":
            print("Saliendo del programa...")
            break
        
        # Obtener función del diccionario
        # .get para obtener la función y devuelve None si no existe
        opcion_menu = menu_ejercicios.get(opcion)
        
        if opcion_menu:
            # Llamar a la función correspondiente contenida en opcion_menu
            opcion_menu()
        else:
            print("Opción no válida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")
            
# Para iniciar el programa
if __name__ == "__main__":
    ejecutar_menu_taller_1()
