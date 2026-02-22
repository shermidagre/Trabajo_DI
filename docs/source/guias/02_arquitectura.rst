Arquitectura del Proyecto
=========================

Este proyecto sigue una estructura estándar de paquetes Python, separando claramente la interfaz gráfica de la lógica de datos.

Estructura de Carpetas
----------------------

* **``gestor_inventario/``**: El paquete principal.
  * **``main.py``**: Punto de entrada de la aplicación.
  * **``configuracionBD.py``** y **``utils.py``**: Scripts para inicializar y localizar la base de datos de forma segura en el sistema del usuario.
  * **``gui/``**: Contiene las clases de GTK3 (``ventanaPrincipal.py``, ``dialogoFormulario.py`` y ``ventanaCategorias.py``).
  * **``bd/``**: Contiene la clase principal para las consultas SQL (``conexionBD.py``).

Persistencia de Datos
---------------------
Se emplea **SQLite** local. La base de datos se genera de forma aislada en el directorio ``home`` del usuario (``~/.gestor_inventario/``) para evitar problemas de permisos de escritura al distribuir la aplicación.