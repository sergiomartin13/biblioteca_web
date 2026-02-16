from abc import ABC, abstractmethod

class RepositorioPublicaciones(ABC): 
        """
    Clase abstracta que define el contrato para cualquier repositorio
    de publicaciones (por ejemplo: base de datos, archivo JSON, memoria, etc.).

    Aplica el principio de inversión de dependencias, permitiendo
    cambiar la implementación sin afectar la lógica de negocio.
    """
    @abstractmethod
    def guardar(self, publicacion):
        """
        Guarda una publicación en el repositorio.

        :param publicacion: Objeto que representa la publicación a almacenar.
        """
        pass

    @abstractmethod
    def cargar_todas(self):
          """
        Recupera todas las publicaciones almacenadas en el repositorio.

        :return: Colección (lista, tupla, etc.) de publicaciones.
        """
        pass

    @abstractmethod
    def borrar(self, titulo):
         """
        Elimina una publicación del repositorio utilizando su título como identificador.

        :param titulo: Título de la publicación a eliminar.
        """
        pass



