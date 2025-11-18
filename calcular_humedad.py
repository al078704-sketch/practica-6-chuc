def calcular_humedad(peso_humedo, peso_seco):
    """
    Fórmula:
    Humedad = (Peso húmedo - Peso seco) / Peso seco * 100%
    """
    humedad = (peso_humedo - peso_seco) / peso_seco * 100
    return humedad

# 1. Ingreso de datos
recipiente_vacio = float(input("Peso del recipiente vacío (g): "))
recipiente_humedo = float(input("Peso del recipiente + suelo húmedo (g): "))
recipiente_seco = float(input("Peso del recipiente + suelo seco (g): "))

# 2. Cálculo de pesos reales del suelo
peso_humedo = recipiente_humedo - recipiente_vacio
peso_seco = recipiente_seco - recipiente_vacio

# 3. Cálculo de humedad
humedad = (peso_humedo - peso_seco) / peso_seco * 100

# 4. Resultado
print(f"\nEl peso húmedo del suelo es: {peso_humedo:.2f} g")
print(f"El peso seco del suelo es: {peso_seco:.2f} g")
print(f"La humedad del suelo es: {humedad:.2f}%")