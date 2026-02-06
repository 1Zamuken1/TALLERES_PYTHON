def consulta_saldo(datos_cuenta):
    """
    Función para consultar saldo de cuenta
    """
    print("╔══════════════════════════════════════╗")
    print("║           CONSULTA SALDO             ║")
    print("╚══════════════════════════════════════╝")
    while True:
        try:
            numero_cuenta_verificacion = int(input("Por favor ingresa tu número de cuenta para consultar el saldo: "))
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
    Realiza la deduccion del saldo tras validar fondos suficientes.
    """
    print("╔══════════════════════════════════════╗")
    print("║           RETIRO DE CUENTA           ║")
    print("╚══════════════════════════════════════╝")
    while True:
        try:
            numero_cuenta_verificacion = int(input("Por favor ingresa tu número de cuenta para validar el usuario: "))
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
            break
        except ValueError:
            print("Entrada no válida. Por favor ingresa un monto válido.")
    datos_cuenta['saldo'] -= monto
    print(f"Retiro exitoso. Nuevo saldo: ${datos_cuenta['saldo']}")
    input("Presiona Enter para continuar...")
        
def consignacion_cuenta(datos_cuenta):
    """
    Suma el monto ingresado al saldo actual en el diccionario.
    """
    print("╔══════════════════════════════════════╗")
    print("║       CONSIGNACIÓN DE CUENTA         ║")
    print("╚══════════════════════════════════════╝")
    while True:
        try:
            numero_cuenta_verificacion = int(input("Por favor ingresa tu número de cuenta para validar el usuario: "))
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
    print(f"COnsignación exitosa. Nuevo saldo: ${datos_cuenta['saldo']}")
    input("Presiona Enter para continuar...")
