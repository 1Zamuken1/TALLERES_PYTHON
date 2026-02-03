def compra_tres_alimentos():
    """
    Un campista compra tres alimentos: una empanada de $2.000, un jugo de $3.000 y una barra de cereal de $1.500.
    Calcula el total a pagar.
    """
    print("---------------------------------------")
    print("|          COMPRA 3 PRODUCTOS         |")
    print("---------------------------------------")
    
    # Solicitar precio empanada
    while True:
        try:
            precio_empanada = float(input("Ingrsa el precio de la empanada: $"))
            if precio_empanada < 0:
                print("El precio no puede ser negativo. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    # Solicitar precio jugo
    while True:
        try:
            precio_jugo = float(input("Ingresa el precio del jugo: $"))
            if precio_jugo < 0:
                print("El precio no puede ser negativo. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    # Solicitar precio de barra de cereal
    while True:
        try:
            precio_barra_cereal = float(input("Ingresa el precio de la barra de ceral: $"))
            if precio_barra_cereal < 0:
                print("El precio no puede ser negativo. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    # Calcular total a pagar
    total = precio_empanada + precio_jugo + precio_barra_cereal
    print(f"Precio Empanada: ${precio_empanada}\nPrecio Jugo: ${precio_jugo}\nPrecio Barra de Cereal: ${precio_barra_cereal}")
    input("Presiona Enter para continuar...")
    