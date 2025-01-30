class Clima:
    def __init__(self):
        self.temperaturas = []

    # Método para ingresar temperaturas diarias
    def ingresar_temperaturas(self):
        for dia in range(7):  # 7 días de la semana
            temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if not self.temperaturas:
            print("No hay datos para calcular el promedio.")
            return 0
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio

# Programa principal
def main():
    print("Promedio semanal del clima - Programación Orientada a Objetos")
    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Llamada al programa principal
main()