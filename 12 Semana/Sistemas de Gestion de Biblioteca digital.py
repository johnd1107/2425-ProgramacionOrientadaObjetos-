import json

# Clase que representa un libro en la biblioteca
class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        self.isbn = isbn  # ISBN es un identificador único para los libros
        self.titulo = titulo
        self.autor = autor  # Autor es una tupla (nombre, apellido)
        self.categoria = categoria

    def __str__(self):
        return f"{self.titulo} por {self.autor[0]} {self.autor[1]} (Categoría: {self.categoria})"

# Clase que representa un usuario de la biblioteca
class Usuario:
    def __init__(self, user_id, nombre):
        self.user_id = user_id  # ID único del usuario
        self.nombre = nombre
        self.libros_prestados = []  # Lista de libros prestados por el usuario

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

# Clase que gestiona la colección de libros, usuarios y préstamos
class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json'):
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()
        self.usuarios = set()  # Conjunto de usuarios registrados
        self.historial_prestamos = []  # Historial de préstamos realizados

    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            return {}

    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.__dict__ for isbn, libro in self.libros.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_libros()

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_libros()
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios.add(usuario)
        print(f"Usuario {usuario.nombre} registrado con éxito.")

    def dar_baja_usuario(self, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario {usuario.nombre} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, user_id):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if libro and usuario:
            if isbn not in [l.isbn for l in usuario.libros_prestados]:
                usuario.libros_prestados.append(libro)
                self.historial_prestamos.append((usuario, libro))
                print(f"Libro {libro.titulo} prestado a {usuario.nombre}.")
            else:
                print("El usuario ya tiene este libro prestado.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
            if libro:
                usuario.libros_prestados.remove(libro)
                print(f"Libro {libro.titulo} devuelto por {usuario.nombre}.")
            else:
                print("Este libro no está prestado a este usuario.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio):
        resultado = [libro for libro in self.libros.values() if criterio.lower() in libro.titulo.lower() or
                     criterio.lower() in libro.autor[0].lower() or
                     criterio.lower() in libro.categoria.lower()]
        if resultado:
            for libro in resultado:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con la búsqueda.")

    def listar_libros_prestados(self, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

# Función que gestiona el menú del sistema
def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Quitar Libro\n3. Registrar Usuario\n4. Dar Baja Usuario\n5. Prestar Libro\n6. Devolver Libro\n7. Buscar Libro\n8. Listar Libros Prestados\n9. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor_nombre = input("Nombre del autor: ")
            autor_apellido = input("Apellido del autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, (autor_nombre, autor_apellido), categoria)
            biblioteca.añadir_libro(libro)
        elif opcion == '2':
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == '3':
            user_id = input("ID del usuario: ")
            nombre = input("Nombre del usuario: ")
            usuario = Usuario(user_id, nombre)
            biblioteca.registrar_usuario(usuario)
        elif opcion == '4':
            user_id = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)
        elif opcion == '5':
            isbn = input("ISBN del libro a prestar: ")
            user_id = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, user_id)
        elif opcion == '6':
            isbn = input("ISBN del libro a devolver: ")
            user_id = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, user_id)
        elif opcion == '7':
            criterio = input("Buscar por título, autor o categoría: ")
            biblioteca.buscar_libro(criterio)
        elif opcion == '8':
            user_id = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(user_id)
        elif opcion == '9':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
