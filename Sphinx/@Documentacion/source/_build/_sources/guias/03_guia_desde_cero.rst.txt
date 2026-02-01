.. _03_guia_desde_cero:

Guía: Tu Propio Proyecto Sphinx Desde Cero
==========================================

Sigue estos pasos para replicar un proyecto de documentación con Sphinx desde cero.

**Paso 1: Preparación del Entorno**
-----------------------------------
1. Crea una carpeta para tu proyecto principal.
2. Dentro, crea y activa un entorno virtual de Python:
   .. code-block:: shell

      python -m venv .venv
      .venv\Scripts\activate

3. Crea las carpetas para el código fuente y la documentación:
   .. code-block:: powershell

      mkdir src docs # Puedes llamar a la de documentación como 'docs' o '@Documentacion'

**Paso 2: Instalar Sphinx**
---------------------------
Con el entorno virtual activado, instala Sphinx:

.. code-block:: shell

   pip install sphinx

**Paso 3: Iniciar el Proyecto Sphinx**
-------------------------------------
Navega a la carpeta de documentación (ej: ``docs``) y ejecuta el asistente:

.. code-block:: shell

   cd docs
   sphinx-quickstart

Responde a las preguntas del asistente:
-   ``Separate source and build directories (y/n) [y]``: Pulsa Enter.
-   ``Project name``: Nombre de tu proyecto.
-   ``Author name(s)``: Tu nombre.
-   ``Project release []``: Versión (ej: 0.0.1).
-   ``Project language [en]``: Escribe `es` para español.

**Paso 4: Escribir Código para Documentar**
------------------------------------------
En tu carpeta ``src``, crea un paquete de Python (ej: ``src/mi_paquete/``). Añade funciones/clases con "docstrings" claros.

.. code-block:: python

   # src/mi_paquete/saludos.py

   def hola_mundo(nombre: str) -> str:
       """Saluda a la persona indicada.

       :param nombre: El nombre de la persona a saludar.
       :type nombre: str
       :return: Un saludo en formato string.
       :rtype: str
       """
       return f"¡Hola, {nombre}!"

**Paso 5: Configurar `conf.py`**
---------------------------------
Edita ``docs/source/conf.py``:
1.  **Añadir ruta a `src`**: Al principio, descomenta `import os` y `sys`, y añade la ruta absoluta a tu carpeta `src`.

    .. code-block:: python

       import os
       import sys
       # Asegúrate que la ruta es correcta para tu proyecto
       sys.path.insert(0, 'C:/ruta/absoluta/a/tu/proyecto/src')

2.  **Activar Extensiones**: Añade `sphinx.ext.autodoc`, `sphinx.ext.napoleon`, `sphinx.ext.viewcode` a la lista `extensions`.

**Paso 6: Crear Contenido `.rst`**
---------------------------------
Dentro de ``docs/source/``, crea ficheros `.rst` (ej: `api.rst`). Usa directivas como `.. automodule::` para documentar código.

.. code-block:: rst

   API de Saludos
   ==============

   .. automodule:: mi_paquete.saludos
      :members:

**Paso 7: Enlazar en `index.rst`**
----------------------------------
En ``docs/source/index.rst``, actualiza ``.. toctree::`` para incluir tus nuevos ficheros.

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      :caption: Contenidos:

      tutorial
      api

**Paso 8: Compilar la Documentación**
-------------------------------------
Desde la carpeta ``docs/`` (la que contiene `conf.py`, `index.rst`, etc.), ejecuta:

.. code-block:: shell

   make html

¡Listo! Abre ``docs/build/html/index.html`` en tu navegador para ver el resultado.