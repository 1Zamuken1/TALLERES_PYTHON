"""
Menu del Taller 2 - Ciclo For y While
Gestiona la navegacion de ejercicios sobre ciclos.

Principio SOLID aplicado:
- Single Responsibility: Solo maneja la logica del taller de ciclos
- Open/Closed: Facil agregar nuevos ejercicios
"""

from Taller2_while_for.Ejercicio1 import ejercicio_suma_pares
from Taller2_while_for.Ejercicio2 import ejercicio_numeros_impares
from Taller2_while_for.Ejercicio3 import ejercicio_dias_entre_citas
from Taller2_while_for.Ejercicio4 import ejercicio_estudiantes_computadores
from Taller2_while_for.Ejercicio5 import ejercicio_contar_palabras
from Taller2_while_for.Ejercicio6 import ejercicio_numeros_primos
from Taller2_while_for.Ejercicio7 import ejercicio_calculadora_completa
from Taller2_while_for.Ejercicio8 import ejercicio_productos_familia
from Taller2_while_for.Ejercicio9 import ejercicio_torneo_futbol
from Taller2_while_for.Ejercicio10 import ejercicio_contar_vocales_consonantes
from Taller2_while_for.Ejercicio11 import ejercicio_numeros_impares_usuario
from Taller2_while_for.Ejercicio12 import ejercicio_numero_secreto
from Taller2_while_for.Ejercicio13 import ejercicio_invertir_palabra
from Taller2_while_for.Ejercicio14 import ejercicio_cuadrados
from Taller2_while_for.Ejercicio15 import ejercicio_personaje_historico
from Taller2_while_for.Ejercicio16 import ejercicio_elementos_quimicos
from Taller2_while_for.Ejercicio17 import ejercicio_formatos_pelicula
from Taller2_while_for.Ejercicio18 import ejercicio_agencia_modelaje
from Taller2_while_for.Ejercicio19 import ejercicio_funcion_matematica
from Taller2_while_for.Ejercicio20 import ejercicio_cambio_dolares
from Taller2_while_for.Ejercicio21 import ejercicio_goles_jugadores
from Hotel.Ejercicio22 import ejercicio_sistema_hotel


def diseno_menu_taller_2_ciclos():
    """
    Imprime la interfaz visual del menu de ciclos en ASCII.
    
    Muestra los 22 ejercicios disponibles sobre ciclos for y while,
    incluyendo el sistema completo de gestion de hotel.
    
    Returns:
        None
    """
    print("╔══════════════════════════════════════════════════╗")
    print("║            TALLER 2 - CICLO FOR & WHILE          ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║   1. Sumar pares del 1 al 100                    ║")
    print("║   2. Mostrar numeros impares del 1 al 100        ║")
    print("║   3. Calculo de dias entre citas                 ║")
    print("║   4. Estudiantes y computadores                  ║")
    print("║   5. Contar letras en frase                      ║")
    print("║   6. Cantidad de primos o si es num primo        ║")
    print("║   7. Calculadora 5 ejercicios para n numeros     ║")
    print("║   8. Productos familia                           ║")
    print("║   9. System FootBall Association                 ║")
    print("║  10. Contar consonantes y vocales de una frase   ║")
    print("║  11. Numeros impares hasta el numero de usuario  ║")
    print("║  12. Juego numero secreto entre 1 y 100          ║")
    print("║  13. Invertir palabra                            ║")
    print("║  14. Cuadrados del 1 al 10                       ║")
    print("║  15. Personaje historico                         ║")
    print("║  16. Elementos quimicos                          ║")
    print("║  17. Formatos de pelicula                        ║")
    print("║  18. Agencia de modelaje                         ║")
    print("║  19. Funcion f(x)=x^3+x^2-5                      ║")
    print("║  20. Cambiar 100 dolares                         ║")
    print("║  21. Partido de futbol de 11 jugadores           ║")
    print("║  22. Sistema de Gestion de Hotel                 ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  0. Regresar                                     ║")
    print("╚══════════════════════════════════════════════════╝")


def ejecutar_menu_taller_2_ciclos():
    """
    Controlador logico del menu de ciclos for y while.
    
    Implementa un ciclo infinito que:
    1. Muestra el menu con todos los ejercicios
    2. Captura la opcion del usuario
    3. Ejecuta el ejercicio correspondiente
    4. Maneja opciones invalidas
    5. Permite regresar al menu principal (opcion "0")
    
    Incluye 22 ejercicios que demuestran el uso de ciclos for y while
    en diversos contextos, desde ejercicios basicos hasta un sistema
    completo de gestion hotelera (Ejercicio 22).
    
    Returns:
        None
    
    Example:
        >>> ejecutar_menu_taller_2_ciclos()
        [Muestra menu]
        Selecciona una opcion: 22
        [Ejecuta sistema de gestion de hotel]
    """
    # Diccionario que mapea opciones a funciones de ejercicios
    menu_ejercicios = {
        "1": ejercicio_suma_pares,
        "2": ejercicio_numeros_impares,
        "3": ejercicio_dias_entre_citas,
        "4": ejercicio_estudiantes_computadores,
        "5": ejercicio_contar_palabras,
        "6": ejercicio_numeros_primos,
        "7": ejercicio_calculadora_completa,
        "8": ejercicio_productos_familia,
        "9": ejercicio_torneo_futbol,
        "10": ejercicio_contar_vocales_consonantes,
        "11": ejercicio_numeros_impares_usuario,
        "12": ejercicio_numero_secreto,
        "13": ejercicio_invertir_palabra,
        "14": ejercicio_cuadrados,
        "15": ejercicio_personaje_historico,
        "16": ejercicio_elementos_quimicos,
        "17": ejercicio_formatos_pelicula,
        "18": ejercicio_agencia_modelaje,
        "19": ejercicio_funcion_matematica,
        "20": ejercicio_cambio_dolares,
        "21": ejercicio_goles_jugadores,
        "22": ejercicio_sistema_hotel,
    }

    while True:
        diseno_menu_taller_2_ciclos()
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "0":
            print("Regresando al menu principal...")
            break
        
        # Obtener funcion del diccionario
        opcion_menu = menu_ejercicios.get(opcion)
        
        if opcion_menu:
            # Llamar a la funcion correspondiente
            opcion_menu()
        else:
            print("Opcion no valida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")
