class GuerreroPolimorfismo:

    def atacar(self, enemigo):
        print("El Guerrero ataca con su espada, causando 10 puntos de daño.")
        enemigo.vida -= 10


class MagoPolimorfismo:

    def atacar(self, enemigo):
        print("El Mago lanza un hechizo, causando 8 puntos de daño.")
        enemigo.vida -= 8


class Enemigo:

    def __init__(self, vida):
        self.vida = vida

    def estado(self):
        print(f"Vida del enemigo: {self.vida}")


# Ejemplo de uso
guerrero = GuerreroPolimorfismo()
mago = MagoPolimorfismo()
enemigo = Enemigo(50)

enemigo.estado()
guerrero.atacar(enemigo)
enemigo.estado()
mago.atacar(enemigo)
enemigo.estado()