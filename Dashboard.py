import os
import subprocess

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/c', 'python', ruta_script], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        else:  # Unix-based systems
            subprocess.Popen(['gnome-terminal', '--', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__) if '__file__' in globals() else os.getcwd()

    unidades = {
        '1': '1 Semana',
        '2': '2 Semana',
        '3': '3 Semana',
        '5': '5 Semana',
        '6': '6 Semana',
        '7': '7 Semana'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key, value in unidades.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion_semana = input("Elige una Semana o '0' para salir: ")
        if eleccion_semana == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_semana in unidades:
            mostrar_scripts(os.path.join(ruta_base, unidades[eleccion_semana]))  # Llama a mostrar_scripts directamente
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_semana):  # Modificada para recibir la ruta de la semana
    try:
        scripts = sorted([f.name for f in os.scandir(ruta_semana) if f.is_file() and f.name.endswith('.py')])

        while True:
            print("\nScripts - Selecciona un script para ver y ejecutar")
            if not scripts:
                print("No hay scripts en esta carpeta.")
                break  # Salir del menú de scripts si no hay scripts
            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Regresar al menú principal")

            eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
            if eleccion_script == '0':
                break
            elif eleccion_script == '9':
                return  # Regresar al menú principal
            else:
                try:
                    eleccion_script = int(eleccion_script) - 1
                    if 0 <= eleccion_script < len(scripts):
                        ruta_script = os.path.join(ruta_semana, scripts[eleccion_script])  # Usa ruta_semana directamente
                        codigo = mostrar_codigo(ruta_script)
                        if codigo:
                            ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                            if ejecutar == '1':
                                ejecutar_codigo(ruta_script)
                            elif ejecutar == '0':
                                print("No se ejecutó el script.")
                            else:
                                print("Opción no válida. Regresando al menú de scripts.")
                            input("\nPresiona Enter para volver al menú de scripts.")
                    else:
                        print("Opción no válida. Por favor, intenta de nuevo.")
                except ValueError:
                    print("Opción no válida. Por favor, intenta de nuevo.")
    except FileNotFoundError:
        print(f"No se encontró la carpeta: {ruta_semana}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    mostrar_menu()
