from servicios.gestor_archivo import GestorArchivo

def main():
    """
    Punto de entrada del programa.
    Aquí se evidencia el uso del constructor y destructor.
    """

    gestor = GestorArchivo()

    archivo = gestor.crear_y_escribir(
        "ejemplo.txt",
        "Este archivo demuestra el uso de __init__ y __del__ en Python."
    )

    print("Fin del programa. El destructor se ejecutará automáticamente.")

if __name__ == "__main__":
    main()
