class Biblioteca:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.publicaciones = self.repositorio.cargar_todas()

    def añadir(self, publicacion):
        # Evitar duplicados
        titulo_lower = publicacion.titulo.lower()
        if any(p.titulo.lower() == titulo_lower
               for p in self.publicaciones):
            return False  # no se añade duplicado
        self.publicaciones.append(publicacion)
        self.repositorio.guardar(publicacion)
        return True

    def prestar(self, titulo):
        for p in self.publicaciones:
            if p.titulo.lower() == titulo.lower():
                return p.prestar()
        return "Publicación no encontrada"

    def devolver(self, titulo):
        for p in self.publicaciones:
            if p.titulo.lower() == titulo.lower():
                return p.devolver()
        return "Publicación no encontrada"

    def listar(self):
        return [
            (type(p).__name__, p.titulo, p.prestado)
            for p in self.publicaciones
        ]

    def borrar(self, titulo):
        for i, p in enumerate(self.publicaciones):
            if p.titulo.lower() == titulo.lower():
                if p.prestado:
                    return "No se puede borrar una publicación prestada"
                del self.publicaciones[i]
                self.repositorio.borrar(titulo)
                return f"Publicación '{titulo}' borrada correctamente"
        return "Publicación no encontrada"
