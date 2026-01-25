from abc import ABC, abstractmethod


class RepositorioPublicaciones(ABC):
    @abstractmethod
    def guardar(self, publicacion):
        pass

    @abstractmethod
    def cargar_todas(self):
        pass

    @abstractmethod
    def borrar(self, titulo):
        pass

