import random

def dividir_dulces():
    """
    Se reparten 48 dulces entre 6 campistas. ¿Cuántos dulces le tocan a cada uno?
    """
    print("---------------------------------------")
    print("|       División de dulces            |")
    print("---------------------------------------")
    
    # Solicitar número de campistas con validación
    while True:
        try:
            numero_campistas = int(input("Ingresa el número de campistas: "))
            if numero_campistas <= 0:
                print("Debe haber al menos 1 campista. Intenta de nuevo")
                continue
            if numero_campistas > 20:
                print("Son demasiados campistas. Máximo 20. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    # Generar cantidad aleatoria de dulces
    total_dulces = random.randint(30, 100)
    
    # Calcular cuántos dulces le tocan a cada uno
    dulces_por_campista = total_dulces // numero_campistas
    dulces_sobrantes = total_dulces % numero_campistas
    
    # Mostrar información general
    print(f"\nTotal de dulces disponibles: {total_dulces}")
    print(f"Número de campistas: {numero_campistas}")
    print(f"\nCada campista recibirá: {dulces_por_campista} dulces")
    print(f"Dulces sobrantes: {dulces_sobrantes}\n")
    
    input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    dividir_dulces()