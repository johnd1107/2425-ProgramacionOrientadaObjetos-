# Programa para calcular el area de una figura geometrica

# Funcion para calcular el area de un circulo
def calcular_area_circulo(radio):
    PI = 3.14159  # Constante para el valor de pi
    return PI * (radio ** 2)


# Funcion para calcular el area de un rectangulo
def calcular_area_rectangulo(base, altura):
    return base * altura

# Funcion para calcular el area de un triangulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Menú principal para seleccionar la figura
def menu_principal():
    print("Seleccione una figura para calcular el area:")
    print("1. circulo")
    print("2. rectangulo")
    print("3. triangulo")


# Inicio del programa
if __name__ == "__main__":
    menu_principal()
    opcion = int(input("Ingrese el numero de la opcion deseada: "))

    if opcion == 1:
        radio = float(input("Ingrese el radio del circulo: "))
        area = calcular_area_circulo(radio)
        print(f"El area del circulo es: {area}")

    elif opcion == 2:
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        area = calcular_area_rectangulo(base, altura)
        print(f"El area del rectangulo es: {area}")

    elif opcion == 3:
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El area del triangulo es: {area}")

    else:
        print("Errror. Por favor, reinicie el programa.")