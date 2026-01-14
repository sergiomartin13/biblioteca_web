class Publicacion:
    def __init__(self, titulo, prestado=False):
        self.titulo = titulo
        self.prestado = prestado

    def prestar(self):
        raise NotImplementedError

    def devolver(self):
        raise NotImplementedError

    def info(self):
        estado = "prestado" if self.prestado else "disponible"
        return f"{self.titulo} - {estado}"


class Libro(Publicacion):
    def prestar(self):
        if self.prestado:
            return "El libro ya estaba prestado"
        else:
            self.prestado = True
            return "Libro prestado correctamente"

    def devolver(self):
        if not self.prestado:
            return "El libro ya está disponible"
        else:
            self.prestado = False
            return "Libro devuelto correctamente"


class Revista(Publicacion):
    def prestar(self):
        return "No se puede prestar una revista"

    def devolver(self):
        return "No se puede devolver una revista"

