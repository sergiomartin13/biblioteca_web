class Biblioteca:
    """
    Clase que representa una biblioteca.

    Se encarga de guardar, prestar, devolver, listar y borrar publicaciones.
    También se conecta con un repositorio para guardar los datos.
    """

    def __init__(self, repositorio):
        """
        Crea una biblioteca nueva y carga las publicaciones guardadas.

        Args:
            repositorio: Objeto que se encarga de guardar y cargar las publicaciones.

        Returns:
            None
        """
        self.repositorio = repositorio
        self.publicaciones = self.repositorio.cargar_todas()

    def añadir(self, publicacion):
        """
        Añade una publicación si no existe otra con el mismo título.

        Args:
            publicacion: Publicación que se quiere añadir.

        Returns:
            bool: True si se añade correctamente.
                  False si ya existe una publicación con el mismo título.
        """
        titulo_lower = publicacion.titulo.lower()

        if any(p.titulo.lower() == titulo_lower for p in self.publicaciones):
            return False

        self.publicaciones.append(publicacion)
        self.repositorio.guardar(publicacion)

        return True

    def prestar(self, titulo):
        """
        Presta una publicación si existe en la biblioteca.

        Args:
            titulo (str): Título de la publicación que se quiere prestar.

        Returns:
            Resultado del método prestar de la publicación
            o el mensaje "Publicación no encontrada" si no existe.
        """
        for p in self.publicaciones:
            if p.titulo.lower() == titulo.lower():
                return p.prestar()

        return "Publicación no encontrada"

    def devolver(self, titulo):
        """
        Devuelve una publicación si existe en la biblioteca.

        Args:
            titulo (str): Título de la publicación que se quiere devolver.

        Returns:
            Resultado del método devolver de la publicación
            o el mensaje "Publicación no encontrada" si no existe.
        """
        for p in self.publicaciones:
            if p.titulo.lower() == titulo.lower():
                return p.devolver()

        return "Publicación no encontrada"

    def listar(self):
        """
        Devuelve una lista con todas las publicaciones.

        Returns:
            list: Lista de tuplas con el tipo de publicación,
                  el título y si está prestada (True o False).
        """
        return [
            (type(p).__name__, p.titulo, p.prestado)
            for p in self.publicaciones
        ]

    def borrar(self, titulo):
        """
        Borra una publicación si existe y no está prestada.

        Args:
            titulo (str): Título de la publicación que se quiere borrar.

        Returns:
            str: Mensaje indicando si se ha borrado correctamente,
                 si no se puede borrar porque está prestada
                 o si no se ha encontrado.
        """
        for i, p in enumerate(self.publicaciones):
            if p.titulo.lower() == titulo.lower():
                if p.prestado:
                    return "No se puede borrar una publicación prestada"

                del self.publicaciones[i]
                self.repositorio.borrar(titulo)

                return f"Publicación '{titulo}' borrada correctamente"

        return "Publicación no encontrada"
