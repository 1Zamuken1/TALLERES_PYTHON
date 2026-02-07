import math

def ejercicio_calculadora_completa():
    """
    Calculadora que permite ingresar n cantidad de números y realizar 5 operaciones:
    suma, resta, multiplicación, división y raíz cuadrada.
    """
    print("---------------------------------------")
    print("|     CALCULADORA COMPLETA            |")
    print("---------------------------------------")
    
    # Solicitar cantidad de números con validación
    while True:
        try:
            cantidad = int(input("\nCuantos numeros deseas ingresar?: "))
            if cantidad < 1:
                print("Debes ingresar al menos 1 numero. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    # Solicitar los números con validación
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                numero = float(input(f"Ingresa el numero {i + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor ingresa un numero valido.")
    
    # Realizar operaciones
    print("\nRESULTADOS DE LAS OPERACIONES")
    
    # 1. SUMA
    suma = sum(numeros)
    print(f"\n1. SUMA de todos los numeros: {suma:.2f}")
    
    # 2. RESTA (resta consecutiva)
    resta = numeros[0]
    for i in range(1, len(numeros)):
        resta -= numeros[i]
    print(f"2. RESTA consecutiva: {resta:.2f}")
    
    # 3. MULTIPLICACIÓN
    multiplicacion = 1
    for numero in numeros:
        multiplicacion *= numero
    print(f"3. MULTIPLICACION de todos los numeros: {multiplicacion:.2f}")
    
    # 4. DIVISIÓN (división consecutiva)
    if all(num != 0 for num in numeros[1:]):
        division = numeros[0]
        for i in range(1, len(numeros)):
            division /= numeros[i]
        print(f"4. DIVISION consecutiva: {division:.2f}")
    else:
        print(f"4. DIVISION consecutiva: No se puede realizar (division por cero)")
    
    # 5. RAÍZ CUADRADA de cada número
    print(f"\n5. RAIZ CUADRADA de cada numero:")
    for i, numero in enumerate(numeros, 1):
        if numero >= 0:
            raiz = math.sqrt(numero)
            print(f"   Raiz de {numero} = {raiz:.4f}")
        else:
            print(f"   Raiz de {numero} = No se puede calcular (numero negativo)")
    
    # Resumen
    print(f"\nNumeros ingresados: {numeros}")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_calculadora_completa()
