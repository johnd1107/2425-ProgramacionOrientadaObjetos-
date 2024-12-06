class PersonajeEncapsulacion:

    def __init__(self, nombre, vida):
        self.__nombre = nombre  # Atributo privado
        self.__vida = vida      # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def get_vida(self):
        return self.__vida

    def set_vida(self, nueva_vida):
        if nueva_vida >= 0:
            self.__vida = nueva_vida
        else:
            print("La vida no puede ser negativa.")

    def atributos(self):
        print(f"{self.__nombre}: Vida = {self.__vida}")


# Ejemplo de uso
personaje = PersonajeEncapsulacion("John", 50)
personaje.atributos()

# Modificar vida usando un método
personaje.set_vida(40)
print(f"Nueva vida: {personaje.get_vida()}")

# Intentar asignar un valor inválido
personaje.set_vida(-10)