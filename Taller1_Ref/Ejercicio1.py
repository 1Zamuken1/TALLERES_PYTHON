def ejercicio_suma_edades():
    """
    Pide al usuario que ingrese la edad de dos personas y muestra la suma total de sus edades.
    """
    print("---------------------------------------")
    print("|            SUMA DE EDADES           |")
    print("---------------------------------------")
    
    # Solicitar primera edad con validación
    while True:
        try:
            edad1 = int(input("Ingresa la edad de la primera persona: "))
            if edad1 < 0:
                print("La edad no puede ser negativa. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido.")
    
    # Solicitar segunda edad con validación
    while True:
        try:
            edad2 = int(input("Ingresa la edad de la segunda persona: "))
            if edad2 < 0:
                print("La edad no puede ser negativa. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido.")
    
    # Calcular y mostrar resultado
    suma = edad1 + edad2
    print(f"\nLa suma total de las edades es: {suma} años")
    input("\nPresiona Enter para continuar...")
