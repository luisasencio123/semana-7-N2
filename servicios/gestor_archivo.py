from modelos.archivo import Archivo


class GestorArchivo:
    """
    Clase de servicio que maneja la lógica relacionada con el archivo.
    """

    def crear_y_escribir(self, nombre, contenido):
        """
        Crea un objeto Archivo y escribe contenido dentro de él.
        """
        archivo = Archivo(nombre)
        archivo.escribir(contenido)

        print("Contenido escrito correctamente.")
        return archivo
