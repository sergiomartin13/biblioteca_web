from flask import Flask, render_template, request, redirect, flash
from adaptadores.repositorio_fichero import RepositorioFichero
from aplicacion.biblioteca import Biblioteca
from dominio.publicacion import Libro, Revista

app = Flask(__name__)
app.secret_key = "clave_super_secreta"  # necesaria para flash

repositorio = RepositorioFichero("biblioteca_hex.txt")
biblioteca = Biblioteca(repositorio)


@app.route("/", methods=["GET"])
def index():
    publicaciones = biblioteca.listar()
    return render_template("index.html", publicaciones=publicaciones)


@app.route("/añadir", methods=["POST"])
def añadir():
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
    titulo = request.form["titulo"]
    mensaje = biblioteca.prestar(titulo)
    flash(mensaje)
    return redirect("/")


@app.route("/devolver", methods=["POST"])
def devolver():
    titulo = request.form["titulo"]
    mensaje = biblioteca.devolver(titulo)
    flash(mensaje)
    return redirect("/")


@app.route("/borrar", methods=["POST"])
def borrar():
    titulo = request.form["titulo"]
    mensaje = biblioteca.borrar(titulo)
    flash(mensaje)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
