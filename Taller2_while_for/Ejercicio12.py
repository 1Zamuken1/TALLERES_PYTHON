import random

def ejercicio_numero_secreto():
    """
    Juego donde el usuario debe adivinar un número secreto entre 1 y 100.
    """
    print("---------------------------------------")
    print("|       JUEGO NUMERO SECRETO          |")
    print("---------------------------------------")
    
    # Generar número secreto aleatorio
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    print("\nHe pensado en un numero entre 1 y 100.")
    print("Intenta adivinarlo!")
    
    # Ciclo del juego
    while True:
        try:
            intento = int(input("\nIngresa tu numero: "))
            intentos += 1
            
            if intento < 1 or intento > 100:
                print("Por favor ingresa un numero entre 1 y 100.")
                continue
            
            if intento < numero_secreto:
                print("El numero secreto es MAYOR. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("El numero secreto es MENOR. Intenta de nuevo.")
            else:
                print(f"\nFelicitaciones! Adivinaste el numero secreto: {numero_secreto}")
                print(f"Lo lograste en {intentos} intento(s).")
                break
                
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_numero_secreto()
