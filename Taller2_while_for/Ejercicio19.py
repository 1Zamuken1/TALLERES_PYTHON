def ejercicio_funcion_matematica():
    """
    Resuelve la función f(x) = x^3 + x^2 - 5 para x del 1 al 10.
    """
    print("---------------------------------------")
    print("|      FUNCION f(x)=x^3+x^2-5         |")
    print("---------------------------------------")
    
    print("\nResolviendo la funcion f(x) = x^3 + x^2 - 5")
    print("Para x tomando valores del 1 al 10:")
    print("\n  x  |  f(x)")
    print("-----|--------")
    
    for x in range(1, 11):
        fx = (x ** 3) + (x ** 2) - 5
        print(f" {x:2}  |  {fx:4}")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_funcion_matematica()
