def ejercicio_productos_familia():
    """
    Gestiona dos listas de compras (papá y mamá), cuenta productos y las unifica sin duplicados.
    """
    print("---------------------------------------")
    print("|      LISTA DE COMPRAS FAMILIAR      |")
    print("---------------------------------------")
    
    # Lista del papá
    print("\n--- LISTA DEL PAPA ---")
    while True:
        try:
            cantidad_papa = int(input("Cuantos productos pidio el papa?: "))
            if cantidad_papa < 0:
                print("La cantidad no puede ser negativa. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    productos_papa = []
    for i in range(cantidad_papa):
        while True:
            producto = input(f"Producto {i + 1} del papa: ").strip().lower()
            if len(producto) == 0:
                print("El producto no puede estar vacio. Intenta de nuevo.")
                continue
            productos_papa.append(producto)
            break
    
    # Lista de la mamá
    print("\n--- LISTA DE LA MAMA ---")
    while True:
        try:
            cantidad_mama = int(input("Cuantos productos pidio la mama?: "))
            if cantidad_mama < 0:
                print("La cantidad no puede ser negativa. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    productos_mama = []
    for i in range(cantidad_mama):
        while True:
            producto = input(f"Producto {i + 1} de la mama: ").strip().lower()
            if len(producto) == 0:
                print("El producto no puede estar vacio. Intenta de nuevo.")
                continue
            productos_mama.append(producto)
            break
    
    # Mostrar resultados
    print("\nRESUMEN DE COMPRAS")
    
    print(f"\nLista del papa ({len(productos_papa)} productos):")
    for i, producto in enumerate(productos_papa, 1):
        print(f"   {i}. {producto.capitalize()}")
    
    print(f"\nLista de la mama ({len(productos_mama)} productos):")
    for i, producto in enumerate(productos_mama, 1):
        print(f"   {i}. {producto.capitalize()}")
    
    # Cantidad total de productos (con duplicados)
    total_productos = len(productos_papa) + len(productos_mama)
    print(f"\nTotal de productos (con posibles duplicados): {total_productos}")
    
    # Unificar listas sin duplicados
    lista_unificada = []
    
    # Agregar productos del papá
    for producto in productos_papa:
        if producto not in lista_unificada:
            lista_unificada.append(producto)
    
    # Agregar productos de la mamá (solo si no están ya)
    for producto in productos_mama:
        if producto not in lista_unificada:
            lista_unificada.append(producto)
    
    # Ordenar alfabéticamente
    lista_unificada.sort()
    
    print(f"\nLista unificada sin duplicados ({len(lista_unificada)} productos):")
    for i, producto in enumerate(lista_unificada, 1):
        print(f"   {i}. {producto.capitalize()}")
    
    # Productos duplicados
    productos_duplicados = total_productos - len(lista_unificada)
    if productos_duplicados > 0:
        print(f"\nSe eliminaron {productos_duplicados} producto(s) duplicado(s).")
    else:
        print(f"\nNo hay productos duplicados.")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_productos_familia()
