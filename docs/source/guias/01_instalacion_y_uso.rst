Instalación e Uso
=================

O Xestor de Inventario está publicado en PyPI, polo que a súa instalación e execución é moi rápida e sinxela.

Requisitos Previos
------------------
* Python 3.8 ou superior.
* Librerías de **GTK3** instaladas no sistema (nativas en Linux, a través de MSYS2 en Windows).

Instalación
-----------
Podes instalar o paquete directamente dende o repositorio oficial usando `pip`:

.. code-block:: bash

   pip install gestor-inventario-samuel

Execución
---------
Unha vez instalado, o paquete rexistra un comando na túa terminal. Para iniciar a aplicación, só tes que escribir:

.. code-block:: bash

   xestor-inventario

Isto abrirá a xanela principal da aplicación e creará automaticamente a base de datos ``inventario.db`` no teu cartafol de usuario (``~/.gestor_inventario/``).