# Ejercicio 10: División de cuenta de almuerzo

print("=== DIVISIÓN DE CUENTA ===\n")

total_almuerzo = float(input("Ingresa el total del almuerzo: $"))
numero_campistas = 3

pago_por_persona = total_almuerzo / numero_campistas

print(f"\nTotal de la cuenta: ${total_almuerzo}")
print(f"Número de campistas: {numero_campistas}")
print(f"Cada campista debe pagar: ${pago_por_persona:.2f}")
