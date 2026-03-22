import os
import tempfile
from adaptadores.repositorio_fichero import RepositorioFichero
from dominio.publicacion import Libro, Revista

#clase test repositorio
class TestRepositorioFichero:
    def setup_method(self):#crear entorno
        self.temp_file = tempfile.NamedTemporaryFile(
            delete=False, mode='w', suffix='.txt'
        )
        self.temp_file.close()
        self.repositorio = RepositorioFichero(self.temp_file.name)

    def teardown_method(self):#limpiar archivos
        os.unlink(self.temp_file.name)

    def test_guardar_libro(self):#guarda libro
        libro = Libro("Libro Test")
        self.repositorio.guardar(libro)
        with open(self.temp_file.name, 'r') as f:
            content = f.read()
            assert "Libro;Libro Test;False\n" == content

    def test_guardar_revista(self):#guarda revista
        revista = Revista("Revista Test")
        self.repositorio.guardar(revista)
        with open(self.temp_file.name, 'r') as f:
            content = f.read()
            assert "Revista;Revista Test;False\n" == content

    def test_cargar_todas_vacio(self):#cargar archivos sin datos
        publicaciones = self.repositorio.cargar_todas()
        assert publicaciones == []

    def test_cargar_todas_con_datos(self):#cargar archivos con datos
        with open(self.temp_file.name, 'w') as f:
            f.write("Libro 1;Libro 1;True\n")#("Libro 1;Libro 1;True\n")
            f.write("Revista;Revista 1;False\n")
        publicaciones = self.repositorio.cargar_todas()
        assert len(publicaciones) == 2
        assert publicaciones[0].titulo == "Libro 1"
        assert publicaciones[0].prestado is True
        assert isinstance(publicaciones[0], Libro)
        assert publicaciones[1].titulo == "Revista 1"
        assert publicaciones[1].prestado is False
        assert isinstance(publicaciones[1], Revista)

    def test_borrar_existente(self):#borrar archivos existentes
        with open(self.temp_file.name, 'w') as f:
            f.write("Libro;Libro 1;False\n")
            f.write("Revista;Revista 1;False\n")
        self.repositorio.borrar("Libro 1")#Borrar Revista 1 también
        with open(self.temp_file.name, 'r') as f:
            content = f.read()
            assert content == "Revista;Revista 1;False\n"

    def test_borrar_no_existente(self):#borrar archivos no existentes
        with open(self.temp_file.name, 'w') as f:
            f.write("Libro;Libro 1;False\n")
        self.repositorio.borrar("No existe")
        with open(self.temp_file.name, 'r') as f:
            content = f.read()
            assert content == "Libro;Libro 1;False\n"
