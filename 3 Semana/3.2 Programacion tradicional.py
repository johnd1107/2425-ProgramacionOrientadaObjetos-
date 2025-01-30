# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):  # 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Programa principal
def main():
    print("Promedio semanal del clima - Programación Tradicional")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Llamada al programa principal
main()