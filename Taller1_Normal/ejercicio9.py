# Ejercicio 9: Cálculo del Índice de Masa Corporal (IMC)

print("=== CÁLCULO DE IMC ===\n")

peso = float(input("Ingresa el peso en kilogramos: "))
estatura = float(input("Ingresa la estatura en metros: "))

imc = peso / (estatura ** 2)

print(f"\nPeso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC: {imc:.2f}")
