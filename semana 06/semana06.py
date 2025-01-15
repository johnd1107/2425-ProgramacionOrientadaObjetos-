# Clase base "Empleado"
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario

    # Método para obtener salario (encapsulación)
    def obtener_salario(self):
        return f"Salario de {self.nombre}: ${self.__salario}"

# Clase derivada "Gerente" que hereda de "Empleado"
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # Llamada al constructor de la clase base
        self.departamento = departamento

    #  (polimorfismo)
    def obtener_salario(self):
        salario = super().obtener_salario().split('$')[1]  # Obtener el salario como string y extraer el valor
        return f"Salario del gerente {self.nombre} (Departamento: {self.departamento}): ${salario}"

# Crear instancias
empleado1 = Empleado("Juan Diaz", 450)
gerente1 = Gerente("Ana Perez", 500, "Ventas")

# Mostrar salarios
print(empleado1.obtener_salario())  # Polimorfismo: utiliza el método de la clase base
print(gerente1.obtener_salario())  # Polimorfismo: sobrescribe el método en la clase derivada
