def ejercicio_cuadrados():
    """
    Imprime un listado con los números del 1 al 10 y sus respectivos cuadrados.
    """
    print("---------------------------------------")
    print("|       CUADRADOS DEL 1 AL 10         |")
    print("---------------------------------------")
    
    print("\nNumero | Cuadrado")
    print("-------|----------")
    
    for numero in range(1, 11):
        cuadrado = numero ** 2
        print(f"  {numero:2}   |   {cuadrado:3}")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_cuadrados()
