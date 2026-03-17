from flask import Flask, render_template, request, redirect, flash
"""
 Importa las funciones necesarias de Flask para crear la app web,
manejar plantillas, recibir datos de formularios, redirecciones y mensajes flash.
"""
from adaptadores.repositorio_fichero import RepositorioFichero
from aplicacion.biblioteca import Biblioteca
from dominio.publicacion import Libro, Revista 
"""
 Importa módulos propios: repositorio para almacenamiento,
 lógica de la biblioteca y clases de dominio para tipos de publicaciones.
"""

app = Flask(__name__)  
"""
Crea la instancia principal de la aplicación Flask.
"""

app.secret_key = "clave_super_secreta"  
"""
Define una clave secreta para habilitar el uso de mensajes flash.
"""
repositorio = RepositorioFichero("biblioteca_hex.txt")  
"""
Crea un repositorio que guarda datos en el fichero "biblioteca_hex.txt".
"""
biblioteca = Biblioteca(repositorio)  
""" 
Crea la instancia de la biblioteca usando el repositorio para persistencia.
"""
"""
Ruta principal que responde a peticiones GET para mostrar la lista de publicaciones (línea 34).
"""
@app.route("/", methods=["GET"])  
def index():
    publicaciones = biblioteca.listar()  
    """
    Obtiene todas las publicaciones almacenadas en la biblioteca.
    """
    return render_template("index.html", publicaciones=publicaciones)  
    """
    Renderiza la plantilla "index.html" pasando las publicaciones para mostrarlas.
    """
"""
Ruta para añadir una nueva publicación, solo acepta POST (envío de formulario)(línea 48).
"""
@app.route("/añadir", methods=["POST"])  
def añadir():
    titulo = request.form["titulo"]  
    """
    Obtiene el título enviado desde el formulario.
    """
    tipo = request.form["tipo"]  
    """
    Obtiene el tipo de publicación (Libro o Revista).
    """
    
    if tipo == "Libro":
        pub = Libro(titulo)  
        """
        Crea un objeto Libro con el título dado.
        """
    else:
        pub = Revista(titulo)  
        """
        Crea un objeto Revista con el título dado.
        """
        
    exito = biblioteca.añadir(pub)  
    """
    Intenta añadir la publicación a la biblioteca, devuelve True si tuvo éxito.
    """

    if not exito:
        flash(f"La publicación '{titulo}' ya existe")  
        """
        Muestra un mensaje de error si la publicación ya estaba registrada.
        """
    else:
        flash(f"Publicación '{titulo}' añadida correctamente")  
        """
        Muestra un mensaje de éxito si se añadió correctamente.
        """
        
    return redirect("/")  
    """
    Redirige a la página principal para mostrar la lista actualizada.
    """

"""
Ruta para prestar una publicación, solo acepta POST (línea 93).
"""
@app.route("/prestar", methods=["POST"])  
def prestar():
    titulo = request.form["titulo"]  
    """
    Obtiene el título de la publicación a prestar.
    """
    mensaje = biblioteca.prestar(titulo)  
    """
    Llama al método prestar y recibe un mensaje con el resultado.
    """
    flash(mensaje)  
    """
    Muestra el mensaje al usuario.
    """
    return redirect("/")  
    """
    Redirige a la página principal.
    """
"""
Ruta para devolver una publicación, solo acepta POST (línea 114).
"""
@app.route("/devolver", methods=["POST"])  
def devolver():
    titulo = request.form["titulo"]  
    """
    Obtiene el título de la publicación a devolver.
    """
    mensaje = biblioteca.devolver(titulo)  
    """
    Llama al método devolver y recibe un mensaje con el resultado.
    """
    flash(mensaje)  
    """
    Muestra el mensaje al usuario.
    """
    return redirect("/")  
    """
    Redirige a la página principal.
    """
"""
Ruta para borrar una publicación, solo acepta POST (línea 153).
"""
@app.route("/borrar", methods=["POST"])  

def borrar():
    titulo = request.form["titulo"]  
    """
    Obtiene el título de la publicación a borrar.
    """
    mensaje = biblioteca.borrar(titulo)  
    """
    Llama al método borrar y recibe un mensaje con el resultado.
    """
    flash(mensaje)  
    """Muestra el mensaje al usuario.
    """
    return redirect("/")  
    """Redirige a la página principal.
    """

if __name__ == "__main__":
    app.run(debug=True)  
    """
    Ejecuta la aplicación en modo debug para facilitar el desarrollo.
    """
