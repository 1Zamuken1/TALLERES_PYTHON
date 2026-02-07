def es_primo(numero):
    """
    Verifica si un número es primo.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def ejercicio_numeros_primos():
    """
    Verifica si un número es primo y/o cuenta cuántos números primos hay hasta ese número.
    """
    print("---------------------------------------")
    print("|        NUMEROS PRIMOS               |")
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
    
    # Verificar si el número es primo
    if es_primo(numero):
        print(f"\nEl numero {numero} ES PRIMO")
    else:
        print(f"\nEl numero {numero} NO ES PRIMO")
    
    # Contar cuántos primos hay hasta ese número
    primos_encontrados = []
    for i in range(2, numero + 1):
        if es_primo(i):
            primos_encontrados.append(i)
    
    cantidad_primos = len(primos_encontrados)
    
    print(f"Cantidad de numeros primos desde 1 hasta {numero}: {cantidad_primos}")
    
    if cantidad_primos > 0:
        print(f"\nNumeros primos encontrados:")
        # Mostrar primos en formato de líneas de 10 números
        for i, primo in enumerate(primos_encontrados):
            print(f"{primo:4}", end=" ")
            if (i + 1) % 10 == 0:
                print()
        print()
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_numeros_primos()
