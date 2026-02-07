def consulta_saldo(datos_cuenta):
    """
    Consulta el saldo de una cuenta bancaria tras verificar el número de cuenta.
    
    Args:
        datos_cuenta (dict): Diccionario con información de la cuenta que contiene:
            - 'numero_cuenta' (int): Número de cuenta asociado
            - 'nombre' (str): Nombre del titular
            - 'saldo' (float): Saldo actual de la cuenta
    
    Return:
        None
    """
    print("╔══════════════════════════════════════╗")
    print("║           CONSULTA SALDO             ║")
    print("╚══════════════════════════════════════╝")
    while True:
        try:
            entrada = input("Por favor ingresa tu número de cuenta para consultar el saldo (o 'regresar' para volver): ")
            if entrada.lower() == 'regresar':
                print("Regresando al menú...")
                return
            numero_cuenta_verificacion = int(entrada)
            if numero_cuenta_verificacion != 123456789:
                print("Número de cuenta incorrecto. No se puede mostrar el saldo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número de cuenta válido.")
            input("Presiona Enter para continuar...")

    print(f"Titular: {datos_cuenta['nombre']}")
    print(f"Saldo actual: ${datos_cuenta['saldo']:.2f}")
    input("Presiona Enter para continuar...")

def retiro_cuenta(datos_cuenta):
    """
    Realiza un retiro de dinero de la cuenta bancaria tras validar el número de cuenta y fondos suficientes.
    Decrementa el saldo del diccionario de datos de la cuenta.
    
    Args:
        datos_cuenta (dict): Diccionario con información de la cuenta que contiene:
            - 'numero_cuenta' (int): Número de cuenta asociado
            - 'saldo' (float): Saldo actual de la cuenta
    
    Return:
        None
    """
    print("╔══════════════════════════════════════╗")
    print("║           RETIRO DE CUENTA           ║")
    print("╚══════════════════════════════════════╝")
    while True:
        try:
            entrada = input("Por favor ingresa tu número de cuenta para validar el usuario (o 'regresar' para volver): ")
            if entrada.lower() == 'regresar':
                print("Regresando al menú...")
                return
            numero_cuenta_verificacion = int(entrada)
            if numero_cuenta_verificacion != 123456789:
                print("Número de cuenta incorrecto. No se puede mostrar el saldo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número de cuenta válido.")
            input("Presiona Enter para continuar...")
    while True:
        try:
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= 0:
                print("Monto inválido. Por favor ingresa un monto válido")
                continue
            if monto > datos_cuenta['saldo']:
                print(f"Saldo insuficiente. Su saldo actual es: ${datos_cuenta['saldo']:.2f}")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor ingresa un monto válido.")
    datos_cuenta['saldo'] -= monto
    print(f"Retiro exitoso. Nuevo saldo: ${datos_cuenta['saldo']:.2f}")
    input("Presiona Enter para continuar...")
        
def consignacion_cuenta(datos_cuenta):
    """
    Realiza una consignación o depósito de dinero en la cuenta bancaria tras validar el número de cuenta.
    Incrementa el saldo del diccionario de datos de la cuenta.
    
    Args:
        datos_cuenta (dict): Diccionario con información de la cuenta que contiene:
            - 'numero_cuenta' (int): Número de cuenta asociado
            - 'saldo' (float): Saldo actual de la cuenta
    
    Return:
        None
    """
    print("╔══════════════════════════════════════╗")
    print("║       CONSIGNACIÓN DE CUENTA         ║")
    print("╚══════════════════════════════════════╝")
    while True:
        try:
            entrada = input("Por favor ingresa tu número de cuenta para validar el usuario (o 'regresar' para volver): ")
            if entrada.lower() == 'regresar':
                print("Regresando al menú...")
                return
            numero_cuenta_verificacion = int(entrada)
            if numero_cuenta_verificacion != 123456789:
                print("Número de cuenta incorrecto. No se puede mostrar el saldo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número de cuenta válido.")
            input("Presiona Enter para continuar...")
    while True:
        try:
            monto = float(input("Ingrese el monto a consignar: "))
            if monto <= 0:
                print("Monto inválido. Por favor ingresa un monto válido")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor ingresa un monto válido.")
    datos_cuenta['saldo'] += monto
    print(f"Consignación exitosa. Nuevo saldo: ${datos_cuenta['saldo']:.2f}")
    input("Presiona Enter para continuar...")
