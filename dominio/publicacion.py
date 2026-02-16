class Publicacion:
    def __init__(self, titulo, prestado=False):
        self.titulo = titulo
        self.prestado = prestado
        # Inicializa la publicación con un título y su estado (prestado o no)

    def prestar(self):
        raise NotImplementedError
        # Método que deben definir las clases hijas para prestar la publicación

    def devolver(self):
        raise NotImplementedError
        # Método que deben definir las clases hijas para devolver la publicación

    def info(self):
        estado = "prestado" if self.prestado else "disponible"
        return f"{self.titulo} - {estado}"
        # Devuelve un texto con el título y si está prestado o disponible


class Libro(Publicacion):
    def prestar(self):
        if self.prestado:
            return "El libro ya estaba prestado"
        self.prestado = True
        return "Libro prestado correctamente"
        # Si no estaba prestado, cambia su estado a prestado

    def devolver(self):
        if not self.prestado:
            return "El libro ya está disponible"
        self.prestado = False
        return "Libro devuelto correctamente"
        # Si estaba prestado, cambia su estado a disponible


class Revista(Publicacion):
    def prestar(self):
        return "No se puede prestar una revista"
        # Las revistas no se pueden prestar

    def devolver(self):
        return "No se puede devolver una revista"
        # Las revistas no se pueden devolver
