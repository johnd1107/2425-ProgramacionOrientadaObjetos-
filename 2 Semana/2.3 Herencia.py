class PersonajeHerencia:

    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def atributos(self):
        print(f"{self.nombre}: Vida = {self.vida}")


class GuerreroHerencia(PersonajeHerencia):

    def __init__(self, nombre, vida, espada):
        super().__init__(nombre, vida)
        self.espada = espada

    def atributos(self):
        super().atributos()
        print(f"Espada = {self.espada}")


# Ejemplo de uso
guerrero = GuerreroHerencia("John", 100, "Espada Valyria")
guerrero.atributos()