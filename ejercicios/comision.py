def ejercicio_comisiones():
    print("╔════════════════════════════════════╗")
    print("║      CÁLCULO DE COMISIONES         ║")
    print("╚════════════════════════════════════╝")
    # 1. Pedir datos y validar
    nombre = input("Ingrese el nombre del vendedor: ")
    
    while True:
        try:
            salario_base = float(input(f"Ingrese el salario base de {nombre}: "))
            if salario_base <= 0:
                print("El salario debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Ingrese un valor numérico")
            
    # validar total
    while True:
        try:
            monto_ventas = float(input("Ingrese el monto total de ventas del mes: "))
            if monto_ventas < 0:
                print("El monto no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Ingrese un número válido para el monto.")
    
    # Validamos cantidad de ventas
    while True:
        try:
            cantidad_ventas = int(input("Ingrese el número de ventas realizadas: "))
            if cantidad_ventas < 0:
                print("La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Ingrese un valor numérico.")

    # Condiciones
    comision = 0.0
    aplica_comision = monto_ventas > 1000000 and cantidad_ventas >= 50

    if aplica_comision:
        comision = salario_base * 0.12
        mensaje_resultado = "¡Felicidades! Cumple con los requisitos para comisión."
    else:
        mensaje_resultado = "No cumple con los requisitos mínimos para comisión este mes."
    
    # 3. Almacenamiento en diccionario
    vendedor_stats = {
        "Nombre": nombre,
        "Salario Base": salario_base,
        "Ventas Totales": monto_ventas,
        "Cant. Ventas": cantidad_ventas,
        "Comisión": comision,
        "Total a Recibir": salario_base + comision
    }

    # 4. Resultados
    print("\n" + "─"*40)
    print(f"RESUMEN PARA: {vendedor_stats['Nombre'].upper()}")
    print(f"Estado: {mensaje_resultado}")
    print("─"*40)
    
    for clave, valor in vendedor_stats.items():
        if isinstance(valor, float):
            print(f"{clave:15}: ${valor:,.2f}")
        else:
            print(f"{clave:15}: {valor}")
    print("─"*40)

if __name__ == "__main__":
    ejercicio_comisiones()