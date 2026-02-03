def calcular_imc():
    """
    Pide el peso (en kilogramos) y la estatura (en metros) de un campista. 
    Calcula su IMC usando la fórmula: IMC = peso / estatura²
    """
    print("---------------------------------------")
    print("|         Cálculo de IMC              |")
    print("---------------------------------------")
    
    # Solicitar peso con validación
    while True:
        try:
            peso = float(input("Ingresa el peso en kilogramos: "))
            if peso <= 0:
                print("El peso debe ser mayor a cero. Intenta de nuevo")
                continue
            if peso > 500:
                print("El peso parece muy alto. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    # Solicitar estatura con validación
    while True:
        try:
            estatura = float(input("Ingresa la estatura en metros: "))
            if estatura <= 0:
                print("La estatura debe ser mayor a cero. Intenta de nuevo")
                continue
            if estatura > 3:
                print("La estatura parece muy alta. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    # Calcular y mostrar resultado
    imc = peso / (estatura ** 2)
    print(f"Peso: {peso}kg\nEstatura: {estatura}m\nTu IMC es: {imc:.2f}")
    input("\nPresiona Enter para continuar...")