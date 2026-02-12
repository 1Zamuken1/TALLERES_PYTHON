"""
Menu del Taller 2 - Cuenta Bancaria
Gestiona la navegacion de operaciones bancarias.

Principio SOLID aplicado:
- Single Responsibility: Solo maneja la logica de cuenta bancaria
- Dependency Inversion: Las funciones bancarias no conocen este menu
"""

from cuenta_bancaria.saludo import saludo_bienvenida
from cuenta_bancaria.menu_cuenta import consulta_saldo, retiro_cuenta, consignacion_cuenta


def diseno_menu_taller_2_banco():
    """
    Imprime la interfaz visual del menu de cuenta bancaria en ASCII.
    
    Muestra las operaciones disponibles:
    - Saludo de bienvenida
    - Consulta de saldo
    - Retiro de fondos
    - Consignacion (deposito)
    
    Returns:
        None
    """
    print("╔═════════════════════════════════════════════════╗")
    print("║           TALLER 2 - CUENTA BANCARIA            ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║  1. Saludo de bienvenida                        ║")
    print("║  2. Consulta de saldo de cuenta                 ║")
    print("║  3. Retiro de cuenta                            ║")
    print("║  4. Consignacion de cuenta                      ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║  0. Regresar                                    ║")
    print("╚═════════════════════════════════════════════════╝")


def ejecutar_menu_taller_2_banco():
    """
    Controlador logico del menu de cuenta bancaria.
    
    Implementa un sistema de operaciones bancarias donde:
    1. Se mantiene un estado de cuenta (numero, nombre, saldo)
    2. Todas las operaciones reciben el diccionario de datos_cuenta
    3. Las operaciones pueden modificar el saldo
    
    El diccionario datos_cuenta actua como una "base de datos" en memoria
    que persiste durante toda la sesion del menu.
    
    Nota: En un sistema real, estos datos estarian en una base de datos
    y se aplicarian principios de encapsulacion mas estrictos.
    
    Returns:
        None
    
    Example:
        >>> ejecutar_menu_taller_2_banco()
        [Muestra menu]
        Selecciona una opcion: 2
        [Muestra saldo actual]
    """
    # Estado de la cuenta bancaria
    # Este diccionario se pasa a todas las funciones bancarias
    datos_cuenta = {
        "numero_cuenta": "123456789",
        "nombre": "Juan Barrios",
        "saldo": 1000.0,
    }
    
    # Diccionario que mapea opciones a funciones bancarias
    menu_ejercicios = {
        "1": saludo_bienvenida,
        "2": consulta_saldo,
        "3": retiro_cuenta,
        "4": consignacion_cuenta,
    }

    while True:
        diseno_menu_taller_2_banco()
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "0":
            print("Regresando al menu principal...")
            break
        
        # Obtener funcion del diccionario
        opcion_menu = menu_ejercicios.get(opcion)
        
        if opcion_menu:
            # Llamar a la funcion pasando los datos de la cuenta
            # Esto permite que las funciones accedan y modifiquen el saldo
            opcion_menu(datos_cuenta)
        else:
            print("Opcion no valida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")
