# Biblioteca Web

Una aplicación web para gestionar una biblioteca usando arquitectura hexagonal en Python con Flask.

## Estructura del Proyecto

- `dominio/`: Contiene las entidades del dominio (Publicacion, Libro, Revista)
- `aplicacion/`: Lógica de aplicación (Biblioteca)
- `puertos/`: Interfaces (RepositorioPublicaciones)
- `adaptadores/`: Implementaciones concretas (RepositorioFichero)
- `templates/`: Plantillas HTML para Flask
- `tests/`: Pruebas unitarias

## Instalación

1. Clona el repositorio
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En Linux/Mac: `source venv/bin/activate`
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecutar la Aplicación

```bash
python app.py
```

## Ejecutar las Pruebas

```bash
python -m pytest tests/ -v
```

### Tipos de Pruebas

- **Pruebas unitarias**: Cubren clases individuales del dominio, aplicación y adaptadores
- **Pruebas de integración**: Verifican el funcionamiento end-to-end de las rutas Flask

## Funcionalidades

- Añadir libros y revistas
- Prestar y devolver libros (las revistas no se pueden prestar)
- Listar todas las publicaciones
- Borrar publicaciones disponibles

## Arquitectura

El proyecto sigue los principios de la Arquitectura Hexagonal (Ports and Adapters), separando claramente el dominio de la infraestructura.