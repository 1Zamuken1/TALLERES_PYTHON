# Ejercicio 2: Promedio de temperaturas del día

print("=== PROMEDIO DE TEMPERATURAS ===\n")

temp_manana = float(input("Temperatura en la mañana (°C): "))
temp_tarde = float(input("Temperatura en la tarde (°C): "))
temp_noche = float(input("Temperatura en la noche (°C): "))

promedio = (temp_manana + temp_tarde + temp_noche) / 3

print(f"\nEl promedio de temperatura del día es: {promedio:.2f} °C")
