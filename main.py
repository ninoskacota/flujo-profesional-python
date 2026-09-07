from importlib import import_module


def mostrar_menu():
    print("\n=== SISTEMA ACADÉMICO COLABORATIVO ===")
    for i in range(1, 31):
        print(f"{i}. Ejecutar tarea {i:02d}")
    print("0. Salir")


def ejecutar_tarea(numero):
    try:
        modulo = import_module(f"funciones.tarea{numero:02d}")
        modulo.ejecutar()
    except ModuleNotFoundError:
        print("Módulo no encontrado.")
    except AttributeError:
        print("La función ejecutar() todavía no fue implementada correctamente.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            print("Fin del programa.")
            break
        if opcion.isdigit() and 1 <= int(opcion) <= 30:
            ejecutar_tarea(int(opcion))
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
