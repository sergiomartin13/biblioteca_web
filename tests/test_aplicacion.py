from unittest.mock import Mock
from aplicacion.biblioteca import Biblioteca
from dominio.publicacion import Libro, Revista


class TestBiblioteca:
    def setup_method(self):
        self.repositorio_mock = Mock()
        self.repositorio_mock.cargar_todas.return_value = []
        self.biblioteca = Biblioteca(self.repositorio_mock)

    def test_añadir_libro_nuevo(self):
        libro = Libro("Nuevo Libro")
        self.repositorio_mock.guardar.return_value = None
        assert self.biblioteca.añadir(libro) is True
        self.repositorio_mock.guardar.assert_called_once_with(libro)
        assert len(self.biblioteca.publicaciones) == 1

    def test_añadir_libro_duplicado(self):
        libro1 = Libro("Libro")
        libro2 = Libro("libro")  # minúscula
        self.biblioteca.publicaciones = [libro1]
        assert self.biblioteca.añadir(libro2) is False
        self.repositorio_mock.guardar.assert_not_called()

    def test_prestar_existente(self):
        libro = Libro("Libro")
        self.biblioteca.publicaciones = [libro]
        resultado = self.biblioteca.prestar("Libro")
        assert resultado == "Libro prestado correctamente"
        assert libro.prestado is True

    def test_prestar_no_existente(self):
        resultado = self.biblioteca.prestar("No existe")
        assert resultado == "Publicación no encontrada"

    def test_devolver_existente(self):
        libro = Libro("Libro", True)
        self.biblioteca.publicaciones = [libro]
        assert (
            self.biblioteca.devolver("Libro") == "Libro devuelto correctamente"
        )
        assert libro.prestado is False

    def test_devolver_no_existente(self):
        assert (
            self.biblioteca.devolver("No existe")
            == "Publicación no encontrada"
        )

    def test_listar(self):
        libro = Libro("Libro", True)
        revista = Revista("Revista")
        self.biblioteca.publicaciones = [libro, revista]
        lista = self.biblioteca.listar()
        assert lista == [
            ("Libro", "Libro", True),
            ("Revista", "Revista", False)
        ]

    def test_borrar_existente_disponible(self):
        libro = Libro("Libro")
        self.biblioteca.publicaciones = [libro]
        self.repositorio_mock.borrar.return_value = None
        assert (
            self.biblioteca.borrar("Libro")
            == "Publicación 'Libro' borrada correctamente"
        )
        self.repositorio_mock.borrar.assert_called_once_with("Libro")
        assert len(self.biblioteca.publicaciones) == 0

    def test_borrar_existente_prestado(self):
        libro = Libro("Libro", True)
        self.biblioteca.publicaciones = [libro]
        assert (
            self.biblioteca.borrar("Libro")
            == "No se puede borrar una publicación prestada"
        )
        self.repositorio_mock.borrar.assert_not_called()

    def test_borrar_no_existente(self):
        assert (
            self.biblioteca.borrar("No existe") == "Publicación no encontrada"
        )
