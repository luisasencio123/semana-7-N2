class Archivo:
    """
    Clase modelo que representa un archivo de texto.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor (__init__):
        Inicializa el nombre del archivo y lo abre en modo escritura.
        Se ejecuta automáticamente cuando se crea el objeto.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, "w")
        print(f"[INIT] Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir(self, texto):
        """
        Método para escribir texto dentro del archivo.
        """
        self.archivo.write(texto + "\n")

    def __del__(self):
        """
        Destructor (__del__):
        Se encarga de cerrar el archivo cuando el objeto deja de existir.
        Puede ejecutarse cuando el programa termina o cuando el objeto
        es eliminado de memoria.
        """
        try:
            self.archivo.close()
            print(f"[DEL] Archivo '{self.nombre_archivo}' cerrado correctamente.")
        except:
            print("[DEL] No se pudo cerrar el archivo.")
