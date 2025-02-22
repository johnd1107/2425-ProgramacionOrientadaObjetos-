# Sistema de gestión de inventarios actualizado
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"

    # Metodo para guardar el producto en formato de texto
    def to_file_string(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    # Cargar productos desde el archivo
    def cargar_inventario(self):
        try:
            with open(self.archivo, "r") as file:
                for line in file:
                    id, nombre, cantidad, precio = line.strip().split(',')
                    producto = Producto(int(id), nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo.")
        except PermissionError:
            print("Error de permisos para acceder al archivo.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el inventario: {e}")

    # Guardar productos en el archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as file:
                for p in self.productos:
                    file.write(p.to_file_string())
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error de permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Ocurrió un error al guardar el inventario: {e}")

    # Añadir un nuevo producto
    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error de ID: el producto ya existe.")
                return
        self.productos.append(producto)
        self.guardar_inventario()
        print(f"Producto {producto.get_nombre()} añadido al inventario.")

    # Eliminar producto por ID
    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                self.guardar_inventario()
                print(f"Producto con ID {id} eliminado.")
                return
        print("Producto no encontrado.")

    # Actualizar cantidad o el precio
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_inventario()
                print(f"Producto con ID {id} actualizado.")
                return
        print("Producto no encontrado.")

    # Buscar producto
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print(f"Productos encontrados con el nombre '{nombre}':")
            for p in encontrados:
                print(p)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    # Mostrar todos los productos
    def mostrar_inventario(self):
        if self.productos:
            print("Inventario de producto:")
            for p in self.productos:
                print(p)
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
                print("Error: Los datos introducidos no son válidos.")

        elif opcion == "2":
            try:
                id = int(input("Introduce el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: El ID debe ser un número.")

        elif opcion == "3":
            try:
                id = int(input("Introduce el ID del producto a actualizar: "))
                cantidad = input("Introduce la nueva cantidad (deja en blanco si no deseas cambiarla): ")
                precio = input("Introduce el nuevo precio (deja en blanco si no deseas cambiarlo): ")

                if cantidad:
                    cantidad = int(cantidad)
                if precio:
                    precio = float(precio)

                inventario.actualizar_producto(id, cantidad if cantidad else None, precio if precio else None)
            except ValueError:
                print("Error: Los datos introducidos no son válidos.")

        elif opcion == "4":
            nombre = input("Introduce el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("¡Gracias!")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    menu()
