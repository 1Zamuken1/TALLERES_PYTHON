def convertir_grados_C_a_F():
    """
    Pide una temperatura en grados Celsius y conviértela a Fahrenheit usando la fórmula: F = C * 1.8 + 32.
    """
    print("---------------------------------------")
    print("|           Convertir °C a °F         |")
    print("---------------------------------------")
    
    # Solicitar temperatura en °C
    try:
        temperatura_C = float(input("Ingresa la temperatura en grados Celsius: "))
    except ValueError:
        print("Por favor ingresa un número válido")
        
    # Aplicamos fórmula F = C * 1.8 + 32
    F = (temperatura_C * 1.8) + 32
    print(f"Temperatura en °C: {temperatura_C}\nTemperatura en °F: {F}")
    input("Presiona Enter para continuar...")
    