.. _02_configuracion_y_archivos:

Configuración y Archivos del Proyecto
=====================================

Esta guía explica el propósito de los archivos clave en un proyecto Sphinx y cómo configurar las opciones básicas.

Glosario de Archivos
--------------------

*   **`@Documentacion/source/conf.py`**:
    El archivo de configuración principal. Aquí defines el nombre del proyecto, autor, idioma, extensiones y la ruta a tu código fuente para la autogeneración de documentación.

*   **`@Documentacion/source/index.rst`**:
    La página de inicio y tabla de contenidos principal. Usa ``.. toctree::`` para enlazar otras páginas y crear el menú de navegación.

*   **`@Documentacion/source/Makefile`** y **`make.bat`**:
    Scripts de ayuda para ejecutar ``sphinx-build`` (ej: ``make html``).

*   **Archivos `.rst` (ej: `tutorial.rst`, `api_reference.rst`)**:
    Ficheros de contenido escritos en reStructuredText.

*   **Archivos `.rst` dentro de `guias/` (ej: `01_comandos_usados.rst`)**:
    Guías específicas.

*   **`@Documentacion/source/_build/`**:
    Carpeta donde Sphinx genera la salida final (ej: sitio web HTML).

*   **`src/`**:
    Carpeta del código Python a documentar.

Configuraciones Clave en `conf.py`
------------------------------------

*   **Información del Proyecto**:
    .. code-block:: python

       project = 'Proyecto de Documentación Samuel'
       copyright = 'Gemini CLI'
       author = 'Gemini CLI el goat'
       release = '0.1'
       language = 'es'

*   **Ruta al Código Fuente**:
    Indica a Sphinx dónde encontrar tu código Python.

    .. code-block:: python

       import os
       import sys
       sys.path.insert(0, 'C:\Users\samue\Documents\dam2\DI-VARIOS_\Random\Sphinx\src')

*   **Extensiones**:
    Funcionalidades adicionales para Sphinx.

    .. code-block:: python

       extensions = [
           'sphinx.ext.autodoc',
           'sphinx.ext.napoleon',
           'sphinx.ext.viewcode',
           'sphinx.ext.todo',
       ]

*   **Configuración de Idioma**:
    .. code-block:: python

       language = 'es'