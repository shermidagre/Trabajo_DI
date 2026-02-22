Arquitectura do Proxecto
========================

Este proxecto segue unha estrutura estándar de paquetes Python, separando claramente a interface gráfica da lóxica de datos.

Estrutura de Cartafoles
-----------------------

* **``gestor_inventario/``**: O paquete principal.
  * **``main.py``**: Punto de entrada da aplicación.
  * **``database_setup.py``** e **``utils.py``**: Scripts para inicializar e localizar a base de datos de forma segura no sistema do usuario.
  * **``gui/``**: Contén as clases de GTK3 (``main_window.py`` e ``form_dialog.py``).
  * **``mi_libreria/``**: Contén a clase principal para as consultas SQL (``conexionBD.py``).

Persistencia de Datos
---------------------
Emprégase **SQLite** local. A base de datos xérase de forma illada no directorio ``home`` do usuario para evitar problemas de permisos de escritura ao distribuír a aplicación.