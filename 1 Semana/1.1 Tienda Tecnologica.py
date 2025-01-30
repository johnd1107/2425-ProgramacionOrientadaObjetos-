class Producto:
    """
    Clase que representa un producto en una tienda.
    """
    def __init__(self, nombre, precio):
        # Inicializa el nombre y el precio del producto
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        # Devuelve una representación en cadena del producto
        return f"Producto: {self.nombre}, Precio: ${self.precio}"


class CarritoDeCompras:
    """
    Clase que representa un carrito de compras.
    """
    def __init__(self):
        # Inicializa una lista para almacenar los productos
        self.productos = []

    def agregar_producto(self, producto):
        # Añade un producto al carrito
        self.productos.append(producto)

    def calcular_total(self):
        # Calcula el costo total de los productos en el carrito
        return sum(producto.precio for producto in self.productos)

    def mostrar_productos(self):
        # Muestra todos los productos en el carrito
        for producto in self.productos:
            print(producto)


# Ejemplo de uso
producto1 = Producto("Laptop", 800)
producto2 = Producto("Mouse", 20)

carrito = CarritoDeCompras()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

print("Productos en el carrito:")
carrito.mostrar_productos()
print(f"Total: ${carrito.calcular_total()}")