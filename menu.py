# Imports Taller 1
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

# Imports Taller 2
from cuenta_bancaria.saludo import saludo_bienvenida
from cuenta_bancaria.menu_cuenta import consulta_saldo, retiro_cuenta, consignacion_cuenta

def diseno_menu_principal():
    """
    Imprime el menú principal de talleres
    """
    print("╔════════════════════════════════════╗")
    print("║    TALLERES PYTHON                 ║")
    print("╠════════════════════════════════════╣")
    print("║  1. Taller 1 - Variables           ║")
    print("║  2. Taller 2 - Ciclo for y While   ║")
    print("╠════════════════════════════════════╣")
    print("║  0. Salir                          ║")
    print("╚════════════════════════════════════╝")

def diseno_menu_taller_1():
    """
    Imprime la interfáz visual del menú en ASCII
    """
    print("╔════════════════════════════════════╗")
    print("║     TALLER 1 - VARIABLES           ║")
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
    print("║  0. Regresar                       ║")
    print("╚════════════════════════════════════╝")
    
def ejecutar_menu_taller_1():
    """ 
    Controlador lógico que administra el acceso a los ejercicios del Taller 1 en base a las entradas del usuario.
    En caso de Ejecutar una opción no existente o letra; el programa regresará al menú al detectar una opción no válida.
    Si el usuario ingresa "0", regresará al menú principal.
    """
    
    # Diccionario que permita acceder a los ejercicios
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
        opcion = input("Selecciona una opción: ")
        if opcion == "0":
            print("Regresando al menú principal...")
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
            
def diseno_menu_taller_2():
    """
    Imprime la interfáz visual del menú en ASCII
    """
    print("╔═════════════════════════════════════════════════╗")
    print("║           TALLER 2 - CUENTA BANCARIA            ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║  1. Saludo de bienvenida                        ║")
    print("║  2. Consulta de saldo de cuenta                 ║")
    print("║  3. Retiro de cuenta                            ║")
    print("║  4. Consignación de cuenta                      ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║  5. Regresar                                    ║")
    print("╚═════════════════════════════════════════════════╝")

def ejecutar_menu_taller_2():
    """
    Controlador lógico que administra el acceso a los ejercicios del Taller 2 en base a las entradas del usuario.
    En caso de Ejecutar una opción no existente o letra; el programa regresará al menú al detectar una opción no válida.
    Si el usuario ingresa "0", regresará al menú principal.
    """
    
    datos_cuenta = {
        "numero_cuenta" : "123456789",
        "nombre" : "Juan Barrios",
        "saldo" : 1000.0,
    }
    
    menu_ejercicios = {
        "1": saludo_bienvenida,
        "2": consulta_saldo,
        "3": retiro_cuenta,
        "4": consignacion_cuenta,
    }

    while True:
        diseno_menu_taller_2()
        opcion = input("Selecciona una opción: ")
        if opcion == "5":
            print("Regresando al menú principal...")
            break
        
        # Obtener función del diccionario
        opcion_menu = menu_ejercicios.get(opcion)
        
        if opcion_menu:
            # Llamar a la función correspondiente contenida en opcion_menu
            opcion_menu(datos_cuenta)  # Pasar datos_cuenta como argumento a las funciones del taller 2
        else:
            print("Opción no válida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")

def diseno_menu_taller_for_y_while():
    """
    Imprime la interfáz visual del menú en ASCII
    """
    print("╔══════════════════════════════════════════════════╗")
    print("║            TALLER 2 - CICLO FOR & WHILE          ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║   1. Sumar pares del 1 al 100                    ║")
    print("║   2. Mostrar números impares del 1 al 100        ║")
    print("║   3. Calculo de días entre citas                 ║")
    print("║   4. Estudiantes y computadores                  ║")
    print("║   5. Contar letras en frase                      ║")
    print("║   6. Cantidad de primos o si es num primo        ║")
    print("║   7. Calculadora 5 ejercicios para n números     ║")
    print("║   8. Productos família                           ║")
    print("║   9. System FootBall Association                 ║")
    print("║  10. Contar consonantes y vocales de una frase   ║")
    print("║  11. Numeros impares hasta el numero de usuario  ║")
    print("║  12. Juego número secreto entre 1 y 100          ║")
    print("║  13. Invertir palabra                            ║")
    print("║  14. Cuadrados del 1 al 10                       ║")
    print("║  15. Personaje histórico                         ║")
    print("║  16. Elementos químicos                          ║")
    print("║  17. Formatos de película                        ║")
    print("║  18. Agencia de modelaje                         ║")
    print("║  19. Función f(x)=x 3 +x 2 -5,                   ║")
    print("║  20. Cambiar 100 dólares                         ║")
    print("║  21. Partido de footbal de 5 jugadores           ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  5. Regresar                                     ║")
    print("╚══════════════════════════════════════════════════╝")
            
def ejecutar_menu_principal():
    """
    Controlador lógico del menú principal que gestiona el acceso a los diferentes talleres.
    """
    menu_talleres = {
        "1": ejecutar_menu_taller_1,
        "2": ejecutar_menu_taller_2,
    }
    
    while True:
        diseno_menu_principal()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "0":
            print("Saliendo del programa...")
            break
        
        # Obtener función del diccionario
        opcion_menu = menu_talleres.get(opcion)
        
        if opcion_menu:
            # Llamar a la función correspondiente del taller
            opcion_menu()
        else:
            print("Opción no válida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")
            
# Para iniciar el programa
if __name__ == "__main__":
    ejecutar_menu_principal()
