# Sistema de Gestión de Blog Modular (Pre-entrega 5)

Este proyecto es un sistema interactivo en consola para gestionar y consultar publicaciones de un blog, refactorizado con una arquitectura modular en Python.

## Estructura del Proyecto

- `main.py`: Controlador principal que ejecuta el bucle de interacción y menú.
- `README.md`: Documentación y guía del proyecto.
- `blog/`: Paquete local con los módulos del sistema.
  - `__init__.py`: Archivo inicializador del paquete.
  - `datos.py`: Estructura de datos con las publicaciones (`posts`).
  - `menu.py`: Función para la interfaz del menú principal.
  - `operaciones.py`: Funciones para listar, buscar y filtrar publicaciones.
  - `validaciones.py`: Reglas de validación para la integridad de los datos.

  ## Ejecución

Para iniciar el programa, ejecutar desde la terminal en la raíz del proyecto:

```bash
python main.py
```bash
python main.py