def ejercicio_numeros_impares_usuario():
    """
    Muestra todos los números impares desde 1 hasta un número ingresado por el usuario.
    """
    print("---------------------------------------")
    print("|     NUMEROS IMPARES HASTA N         |")
    print("---------------------------------------")
    
    # Solicitar número con validación
    while True:
        try:
            numero = int(input("\nIngresa un numero entero positivo: "))
            if numero < 1:
                print("El numero debe ser mayor o igual a 1. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    # Generar números impares
    impares = []
    for i in range(1, numero + 1):
        if i % 2 != 0:
            impares.append(str(i))
    
    # Mostrar resultado
    print(f"\nNumeros impares desde 1 hasta {numero}:")
    print(", ".join(impares))
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_numeros_impares_usuario()
