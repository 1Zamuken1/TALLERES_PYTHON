import random

def dividir_dulces():
    """
    Se reparten 48 dulces entre 6 campistas. ¿Cuántos dulces le tocan a cada uno?
    """
    
    total_dulces = random.randint(30, 100)
    numero_campistas = 6
    
    dulces_por_campista = total_dulces // numero_campistas
    dulces_sobrantes = total_dulces % numero_campistas
    
    print("---------------------------------------")
    print("|            DIVIDIR DULCES           |")
    print("---------------------------------------")
    
    print(f"Total de dulces: {total_dulces}\nNúmero de campistas: {numero_campistas}\nDulces por campista: {dulces_por_campista}\nSobran: {dulces_sobrantes} dulces")
    input("Presiona Enter para continuar...")