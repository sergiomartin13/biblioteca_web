from dominio.publicacion import Libro, Revista
from puertos.repositorio_publicaciones import RepositorioPublicaciones


class RepositorioFichero(RepositorioPublicaciones):
    def __init__(self, nombre_fichero):

        # Inicia el objeto para ponerle el nombre
        #Args: nombre_fichero: Nombre del fichero
        #Returns: Nada
        self.nombre_fichero = nombre_fichero

    def guardar(self, publicacion):

        #Guarda todas las publicaciones al fichero
        #Args: publicacion
        #Returns: Nada
        with open(self.nombre_fichero, "a", encoding="utf-8") as f:
            linea = (
                f"{type(publicacion).__name__};{publicacion.titulo};"
                f"{publicacion.prestado}\n"
            )
            f.write(linea)

    def cargar_todas(self):
        #Carga todas las publicaciones del fichero al programa
        #Args: Nada
        #Returns: Publicaciones
        publicaciones = []
        try:
            with open(self.nombre_fichero, "r", encoding="utf-8") as f:
                for linea in f:
                    tipo, titulo, prestado = linea.strip().split(";")
                    prestado = prestado == "True"
                    if tipo == "Libro":
                        publicaciones.append(Libro(titulo, prestado))
                    elif tipo == "Revista":
                        publicaciones.append(Revista(titulo))
        except FileNotFoundError:
            pass
        return publicaciones

    def borrar(self, titulo):

        # 
        #Args: título
        #Returns: Nada
        publicaciones = self.cargar_todas()
        publicaciones_filtradas = [
            p for p in publicaciones
            if p.titulo.lower() != titulo.lower()
        ]
        # Reescribir el archivo con las publicaciones filtradas
        with open(self.nombre_fichero, "w", encoding="utf-8") as f:
            for pub in publicaciones_filtradas:
                f.write(f"{type(pub).__name__};{pub.titulo};{pub.prestado}\n")
