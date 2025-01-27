# Ejemplo de uso de Constructores (__init__) y Destructores (__del__)

class Archivo:
    def __init__(self, nombre_archivo, modo):
        """
        Constructor: abre el archivo."""
        self.archivo = open(nombre_archivo, modo)
        print(f"Archivo '{nombre_archivo}' abierto en modo '{modo}'.")

    def __del__(self):
        """
        Destructor: cierra el archivo si está abierto.
        """
        self.archivo.close()
        print("Archivo cerrado.")

# Demostración del uso de la clase Archivo
if __name__ == "__main__":
    archivo = Archivo("ejemplo.txt", "w")
    archivo.archivo.write("Ejemplo de constructores y destructores.\n")
    print("Fin del programa.")
