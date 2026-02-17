def ejercicio_cesta_compras():
    cesta = {}
    total = 0

    print("╔══════════════════════════════════════════╗")
    print("║     SIMULADOR DE CESTA DE COMPRAS        ║")
    print("╠══════════════════════════════════════════╣")
    print("║ Escriba 'FIN' en el artículo para salir  ║")
    print("╚══════════════════════════════════════════╝")

    # 1. Bucle de llenado de la cesta
    while True:
        articulo = input("Artículo: ").strip()
        
        # Condición de salida
        if articulo.upper() == "FIN":
            break
        
        # Validación del precio
        while True:
            try:
                precio = float(input(f"Precio de '{articulo}': "))
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un precio numérico válido.")

        # Añadir al diccionario
        cesta[articulo] = precio

    # 2. Mostrar resultados y calcular total
    if not cesta:
        print("\n[!] La cesta está vacía.")
    else:
        # Recorremos el diccionario para mostrar y sumar
        for item, valor in cesta.items():
            print(f"{item} {valor}")
            total += valor
        
        print(f"TOTAL {total}")

if __name__ == "__main__":
    ejercicio_cesta_compras()