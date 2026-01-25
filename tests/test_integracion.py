import pytest
import tempfile
import os
from flask import Flask
from adaptadores.repositorio_fichero import RepositorioFichero
from aplicacion.biblioteca import Biblioteca
from dominio.publicacion import Libro, Revista


@pytest.fixture
def app():
    # Crear archivo temporal para pruebas
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    temp_file.close()

    # Crear app de prueba
    app = Flask(__name__)
    app.secret_key = "test_secret"
    app.config['TESTING'] = True

    repositorio = RepositorioFichero(temp_file.name)
    biblioteca = Biblioteca(repositorio)

    @app.route("/", methods=["GET"])
    def index():
        publicaciones = biblioteca.listar()
        return f"Publicaciones: {publicaciones}"

    @app.route("/añadir", methods=["POST"])
    def añadir():
        from flask import request, redirect, flash
        titulo = request.form["titulo"]
        tipo = request.form["tipo"]
        if tipo == "Libro":
            pub = Libro(titulo)
        else:
            pub = Revista(titulo)
        exito = biblioteca.añadir(pub)
        if not exito:
            flash(f"La publicación '{titulo}' ya existe")
        else:
            flash(f"Publicación '{titulo}' añadida correctamente")
        return redirect("/")

    @app.route("/prestar", methods=["POST"])
    def prestar():
        from flask import request, redirect, flash
        titulo = request.form["titulo"]
        mensaje = biblioteca.prestar(titulo)
        flash(mensaje)
        return redirect("/")

    @app.route("/devolver", methods=["POST"])
    def devolver():
        from flask import request, redirect, flash
        titulo = request.form["titulo"]
        mensaje = biblioteca.devolver(titulo)
        flash(mensaje)
        return redirect("/")

    yield app

    # Limpiar archivo temporal
    os.unlink(temp_file.name)


@pytest.fixture
def client(app):
    return app.test_client()


class TestIntegracion:
    def test_index_vacio(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert "Publicaciones: []" in response.get_data(as_text=True)

    def test_añadir_libro(self, client):
        response = client.post('/añadir', data={'titulo': 'Nuevo Libro', 'tipo': 'Libro'}, follow_redirects=True)
        assert response.status_code == 200
        assert "Publicaciones: [('Libro', 'Nuevo Libro', False)]" in response.get_data(as_text=True)

    def test_añadir_revista(self, client):
        response = client.post('/añadir', data={'titulo': 'Nueva Revista', 'tipo': 'Revista'}, follow_redirects=True)
        assert response.status_code == 200
        assert "Publicaciones: [('Revista', 'Nueva Revista', False)]" in response.get_data(as_text=True)

    def test_añadir_duplicado(self, client):
        client.post('/añadir', data={'titulo': 'Libro', 'tipo': 'Libro'})
        response = client.post('/añadir', data={'titulo': 'libro', 'tipo': 'Libro'}, follow_redirects=True)
        assert response.status_code == 200
        # Debería tener solo uno
        data = response.get_data(as_text=True)
        assert "Publicaciones: [('Libro', 'Libro', False)]" in data

    def test_prestar_libro(self, client):
        client.post('/añadir', data={'titulo': 'Libro', 'tipo': 'Libro'})
        response = client.post('/prestar', data={'titulo': 'Libro'}, follow_redirects=True)
        assert response.status_code == 200
        assert "Publicaciones: [('Libro', 'Libro', True)]" in response.get_data(as_text=True)

    def test_prestar_revista(self, client):
        client.post('/añadir', data={'titulo': 'Revista', 'tipo': 'Revista'})
        response = client.post('/prestar', data={'titulo': 'Revista'}, follow_redirects=True)
        assert response.status_code == 200
        # Revista no cambia de estado
        assert "Publicaciones: [('Revista', 'Revista', False)]" in response.get_data(as_text=True)

    def test_devolver_libro(self, client):
        client.post('/añadir', data={'titulo': 'Libro', 'tipo': 'Libro'})
        client.post('/prestar', data={'titulo': 'Libro'})
        response = client.post('/devolver', data={'titulo': 'Libro'}, follow_redirects=True)
        assert response.status_code == 200
        assert "Publicaciones: [('Libro', 'Libro', False)]" in response.get_data(as_text=True)

    def test_prestar_no_existente(self, client):
        response = client.post('/prestar', data={'titulo': 'No existe'}, follow_redirects=True)
        assert response.status_code == 200
        assert "Publicaciones: []" in response.get_data(as_text=True)