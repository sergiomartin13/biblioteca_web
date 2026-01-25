import pytest
from dominio.publicacion import Publicacion, Libro, Revista


class TestPublicacion:
    def test_info_disponible(self):
        pub = Publicacion("Test", False)
        assert pub.info() == "Test - disponible"

    def test_info_prestado(self):
        pub = Publicacion("Test", True)
        assert pub.info() == "Test - prestado"

    def test_prestar_abstracto(self):
        pub = Publicacion("Test")
        with pytest.raises(NotImplementedError):
            pub.prestar()

    def test_devolver_abstracto(self):
        pub = Publicacion("Test")
        with pytest.raises(NotImplementedError):
            pub.devolver()


class TestLibro:
    def test_prestar_disponible(self):
        libro = Libro("El Quijote")
        assert libro.prestar() == "Libro prestado correctamente"
        assert libro.prestado is True

    def test_prestar_ya_prestado(self):
        libro = Libro("El Quijote", True)
        assert libro.prestar() == "El libro ya estaba prestado"
        assert libro.prestado is True

    def test_devolver_disponible(self):
        libro = Libro("El Quijote")
        assert libro.devolver() == "El libro ya está disponible"
        assert libro.prestado is False

    def test_devolver_prestado(self):
        libro = Libro("El Quijote", True)
        assert libro.devolver() == "Libro devuelto correctamente"
        assert libro.prestado is False


class TestRevista:
    def test_prestar(self):
        revista = Revista("National Geographic")
        assert revista.prestar() == "No se puede prestar una revista"
        assert revista.prestado is False

    def test_devolver(self):
        revista = Revista("National Geographic")
        assert revista.devolver() == "No se puede devolver una revista"
        assert revista.prestado is False
