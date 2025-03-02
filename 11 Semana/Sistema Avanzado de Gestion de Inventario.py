import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Convertir el producto a diccionario para su serialización en JSON
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    # Representación en cadena del producto
    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Diccionario: llave = id, valor = objeto Producto
        self.cargar_inventario()

    # Cargar el inventario desde un archivo JSON
    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                data = json.load(file)
                # Convertir las llaves a int y crear instancias de Producto
                self.productos = {int(k): Producto(**v) for k, v in data.items()}
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado. Se creará uno nuevo.")
            self.productos = {}
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. Se iniciará un inventario vacío.")
            self.productos = {}
        except Exception as e:
            print(f"Ocurrió un error al cargar el inventario: {e}")
            self.productos = {}

    # Guardar el inventario en un archivo JSON
    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                json.dump({k: v.to_dict() for k, v in self.productos.items()}, file, indent=4)
            print("Inventario guardado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al guardar el inventario: {e}")

    # Añadir un nuevo producto
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: el producto con este ID ya existe.")
            return
        self.productos[producto.get_id()] = producto
        self.guardar_inventario()
        print(f"Producto '{producto.get_nombre()}' añadido al inventario.")

    # Eliminar un producto por ID
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print(f"Producto con ID {id} eliminado.")
        else:
            print("Producto no encontrado.")

    # Actualizar cantidad o precio de un producto
    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
            print(f"Producto con ID {id} actualizado.")
        else:
            print("Producto no encontrado.")

    # Buscar productos por nombre (búsqueda insensible a mayúsculas/minúsculas)
    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            print(f"Productos encontrados con el nombre '{nombre}':")
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    # Mostrar todos los productos en el inventario
    def mostrar_inventario(self):
        if self.productos:
            print("Inventario de productos:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                id = int(input("Introduce el ID del producto: "))
                nombre = input("Introduce el nombre del producto: ")
                cantidad = int(input("Introduce la cantidad: "))
                precio = float(input("Introduce el precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Datos inválidos.")

        elif opcion == "2":
            try:
                id = int(input("Introduce el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: El ID debe ser un número.")

        elif opcion == "3":
            try:
                id = int(input("Introduce el ID del producto a actualizar: "))
                cantidad_input = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")
                precio_input = input("Introduce el nuevo precio (deja en blanco para no cambiar): ")
                cantidad = int(cantidad_input) if cantidad_input else None
                precio = float(precio_input) if precio_input else None
                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("Error: Datos inválidos.")

        elif opcion == "4":
            nombre = input("Introduce el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("¡Gracias por usar el sistema de gestión de inventarios!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
