Instalación y Uso
=================

El Gestor de Inventario está publicado en PyPI, por lo que su instalación y ejecución es muy rápida y sencilla.

Requisitos Previos
------------------
* Python 3.8 o superior.
* Librerías de **GTK3** instaladas en el sistema (nativas en Linux, a través de WSL o MSYS2 en Windows).

Instalación
-----------
Puedes instalar el paquete directamente desde el repositorio oficial usando `pip`:

.. code-block:: bash

   pip install gestor-inventario-samuel

Ejecución
---------
Una vez instalado, el paquete registra un comando en tu terminal. Para iniciar la aplicación, solo tienes que escribir:

.. code-block:: bash

   arrancar-inventario

Esto abrirá la ventana principal de la aplicación y creará automáticamente la base de datos ``inventario.db`` en tu carpeta de usuario (``~/.gestorInventario/``).