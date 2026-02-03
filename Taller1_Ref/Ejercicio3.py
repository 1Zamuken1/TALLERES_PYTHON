def dividir_litros_agua():
    """
    Se tienen 10 litros de agua y 4 campistas. Calcula cuántos litros le tocan a cada uno.
    """
    print("---------------------------------------")
    print("|        DIVIDIR LITROS DE AGUA       |")
    print("---------------------------------------")
    
    # Solicitar litros de agua
    while True:
        try:
            litros_agua = float(input("Ingresa la cantidad de litros de agua: "))
            if litros_agua < 0:
                print("Los litros no pueden ser negativos. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")

    # Solicitar número de campistas
    while True:
        try:
            numero_campistas = int(input("Ingresa el número de campistas: "))
            if numero_campistas < 0:
                print("El número no puede ser negativo. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    # División de litros
    agua_por_campista = litros_agua / numero_campistas
    print(f"La cantidad de agua correspondiente a cada campista es de {agua_por_campista} Litros")
    input("Presiona Enter para continuar...")
    