def kilometros_caminados():
    """
    Un campista camina 3 km por la mañana, 2.5 km por la tarde y 1.5 km por la noche. ¿Cuántos km caminó en total?
    """
    print("---------------------------------------")
    print("|        Kilómetros recorridos        |")
    print("---------------------------------------")
    
    # Solicitar kilómetros de la mañana
    while True:
        try:
            kilometros_manana = float(input("Ingresa la cantidad de kilómetros recorridos por la mañana: "))
            if kilometros_manana < 0:
                print("Los kilómetros no pueden ser negativos. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    # Solicitar kilómetros de la tarde
    while True:
        try:
            kilometros_tarde = float(input("Ingresa la cantidad de kilómetros recorridos por la tarde: "))
            if kilometros_tarde < 0:
                print("Los kilómetros no pueden ser negativos. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
            
    # Solicitar kilómetros de la noche
    while True:
        try:
            kilometros_noche = float(input("Ingresa la cantidad de kilómetros recorridos por la noche: "))
            if kilometros_noche < 0:
                print("Los kilómetros no pueden ser negativos. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    # Suma de kilómetros
    suma_kilometros = kilometros_manana + kilometros_tarde + kilometros_noche
    print(f"El total de la cantidad caminada es de {suma_kilometros}Km")
    input("Presiona Enter para continuar...")