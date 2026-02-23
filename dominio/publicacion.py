class Publicacion:
    """
    Clase base que representa una publicación genérica de una biblioteca.
    """

    def __init__(self, titulo: str, prestado: bool = False):
        """
        Inicializa una nueva publicación.

        Parámetros:
        titulo (str): Título de la publicación.
        prestado (bool): Estado inicial de la publicación.
                         True si está prestada, False si está disponible.
                         Por defecto es False.

        Valor de retorno:
        None
        """
        self.titulo = titulo
        self.prestado = prestado

    def prestar(self) -> str:
        """
        Método abstracto para prestar la publicación.

        Parámetros:
        Ninguno.

        Valor de retorno:
        str: Mensaje indicando el resultado de la operación.
        """
        raise NotImplementedError

    def devolver(self) -> str:
        """
        Método abstracto para devolver la publicación.

        Parámetros:
        Ninguno.

        Valor de retorno:
        str: Mensaje indicando el resultado de la operación.
        """
        raise NotImplementedError

    def info(self) -> str:
        """
        Devuelve información sobre la publicación.

        Parámetros:
        Ninguno.

        Valor de retorno:
        str: Cadena con el título de la publicación y su estado
             ('prestado' o 'disponible').
        """
        estado = "prestado" if self.prestado else "disponible"
        return f"{self.titulo} - {estado}"


class Libro(Publicacion):
    """
    Clase que representa un libro, heredando de Publicacion.
    Permite prestar y devolver libros.
    """

    def prestar(self) -> str:
        """
        Marca el libro como prestado si está disponible.

        Parámetros:
        Ninguno.

        Valor de retorno:
        str: Mensaje indicando si el libro fue prestado correctamente
             o si ya estaba prestado.
        """
        if self.prestado:
            return "El libro ya estaba prestado"
        self.prestado = True
        return "Libro prestado correctamente"

    def devolver(self) -> str:
        """
        Marca el libro como disponible si estaba prestado.

        Parámetros:
        Ninguno.

        Valor de retorno:
        str: Mensaje indicando si el libro fue devuelto correctamente
             o si ya estaba disponible.
        """
        if not self.prestado:
            return "El libro ya está disponible"
        self.prestado = False
        return "Libro devuelto correctamente"


class Revista(Publicacion):
    """
    Clase que representa una revista, heredando de Publicacion.
    Las revistas no pueden prestarse ni devolverse.
    """

    def prestar(self) -> str:
        """
        Intenta prestar una revista.

        Parámetros:
        Ninguno.

        Valor de retorno:
        str: Mensaje indicando que no se puede prestar una revista.
        """
        return "No se puede prestar una revista"

    def devolver(self) -> str:
        """
        Intenta devolver una revista.

        Parámetros:
        Ninguno.

        Valor de retorno:
        str: Mensaje indicando que no se puede devolver una revista.
        """
        return "No se puede devolver una revista"
