import pytest
from dominio.publicacion import Publicacion, Libro, Revista


class TestPublicacion:
    """
    Pruebas para la clase Publicacion
    """

    def test_info_disponible(self):
        """
        Revisa que esté disponible y dice "disponible" cuando no está prestado
        """

        pub = Publicacion("Test", False)
        assert pub.info() == "Test - disponible"

    def test_info_prestado(self):
        """
        Revisa que diga que está "prestado" cuando si está prestado
        """

        pub = Publicacion("Test", True)
        assert pub.info() == "Test - prestado"

    def test_prestar_abstracto(self):
        """
        Confirma que el metodo prestar no sirve en la clase base
        NotImplementedError: Error porque el método no tiene codigo todavía
        """

        pub = Publicacion("Test")
        with pytest.raises(NotImplementedError):
            pub.prestar()

    def test_devolver_abstracto(self):
        """
         Confirma que el metodo devolver no sirve en la clase base
         NotImplementedError: Error porque el método no tiene codigo todavía
         """

       
        pub = Publicacion("Test")
        with pytest.raises(NotImplementedError):
            pub.devolver()


class TestLibro:
    """
    Pruebas para ver cómo funcionan los préstamos de libros
    """

    def test_prestar_disponible(self):
        """
        Presta un libro que está libre y cambia su estado a prestado
        """

        libro = Libro("El Quijote")
        assert libro.prestar() == "Libro prestado correctamente"
        assert libro.prestado is True

    def test_prestar_ya_prestado(self):
        """
        Avisa que no se puede prestar un libro que ya está prestado
        """

        libro = Libro("El Quijote", True)
        assert libro.prestar() == "El libro ya estaba prestado"
        assert libro.prestado is True

    def test_devolver_disponible(self):
        """
        Avisa que no puedes devolver un libro que ya está en la biblioteca
        """

        libro = Libro("El Quijote")
        assert libro.devolver() == "El libro ya está disponible"
        assert libro.prestado is False

    def test_devolver_prestado(self):
        """
        Devuelve un libro prestado y lo pone como disponible
        """

        libro = Libro("El Quijote", True)
        assert libro.devolver() == "Libro devuelto correctamente"
        assert libro.prestado is False


class TestRevista:
    """
    Pruebas para confirmar que las revistas no se pueden prestar
    """

    def test_prestar(self):
        """
        Verifica que no se puede prestar una revista
        """

        revista = Revista("National Geographic")
        assert revista.prestar() == "No se puede prestar una revista"
        assert revista.prestado is False

    def test_devolver(self):
        """
        Verifica que no se puede devolver una revista
        """

        revista = Revista("National Geographic")
        assert revista.devolver() == "No se puede devolver una revista"
        assert revista.prestado is False
