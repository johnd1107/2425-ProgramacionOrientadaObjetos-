# Clase base Personaje
class PersonajeAbstraccion:

    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def atributos(self):
        print(f"{self.nombre}: Vida = {self.vida}")

    def atacar(self, enemigo):
        daño = self.calcular_daño(enemigo)
        enemigo.vida = max(0, enemigo.vida - daño)
        print(f"{self.nombre} ha hecho {daño} puntos de daño a {enemigo.nombre}.")

    def calcular_daño(self, enemigo):
        raise NotImplementedError("Este método debe ser implementado por una subclase")


class GuerreroAbstraccion(PersonajeAbstraccion):

    def calcular_daño(self, enemigo):
        return 10  # Daño fijo para el Guerrero


class MagoAbstraccion(PersonajeAbstraccion):

    def calcular_daño(self, enemigo):
        return 8  # Daño fijo para el Mago


# Ejemplo de uso
guerrero = GuerreroAbstraccion("Ares", 100)
mago = MagoAbstraccion("John", 80)

guerrero.atributos()
mago.atributos()
guerrero.atacar(mago)
mago.atacar(guerrero)
