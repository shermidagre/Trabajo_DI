.. _01_comandos_usados:

Comandos Utilizados para la Configuración
=======================================

Esta guía resume los comandos principales que se usaron para configurar este proyecto de Sphinx desde una terminal PowerShell.

**1. Creación de Directorios**
-----------------------------
Primero, creamos las carpetas necesarias para el código fuente y la documentación.

.. code-block:: powershell

   mkdir src "@Documentacion"

**2. Instalación de Sphinx**
---------------------------
Añadimos Sphinx a ``requirements.txt`` y lo instalamos usando el pip del entorno virtual.

.. code-block:: powershell

   # Añadir 'sphinx' a requirements.txt
   Set-Content -Path requirements.txt -Value "sphinx"

   # Instalar usando la ruta completa al python del .venv
   # Asegúrate que la ruta a tu proyecto es correcta
   $python_exe = "C:\Users\samue\Documents\dam2\DI-VARIOS_\Random\Sphinx\.venv\Scripts\python.exe"
   & $python_exe -m pip install -r requirements.txt

**3. Inicialización del Proyecto Sphinx**
----------------------------------------
Usamos ``sphinx-quickstart`` en modo no interactivo para crear el esqueleto del proyecto. Se ejecutó desde la carpeta ``@Documentacion\source``.

Parámetros clave:
- ``-q``: Modo silencioso.
- ``-p``: Nombre del proyecto.
- ``-a``: Nombre del autor.
- ``-v``: Versión.
- ``--language``: Idioma para la documentación.

.. code-block:: powershell

   # Ruta completa al ejecutable de sphinx-quickstart
   $sphinx_qs = "C:\Users\samue\Documents\dam2\DI-VARIOS_\Random\Sphinx\.venv\Scripts\sphinx-quickstart.exe"
   & $sphinx_qs -q -p "Proyecto de Documentación Gemini" -a "Gemini CLI" -v "0.1" --language="es" .

**4. Configuración del `conf.py`**
---------------------------------
Editamos ``conf.py`` para:
- Añadir la ruta absoluta a ``src``.
- Activar extensiones: ``autodoc``, ``napoleon``, ``viewcode``, ``todo``.

**5. Creación de Contenido `.rst`**
-----------------------------------
Se crearon ficheros como ``tutorial.rst``, ``api_reference.rst`` y las guías dentro de ``source/guias/``. Se enlazaron en ``index.rst``.

**6. Compilación de la Documentación HTML**
------------------------------------------
Para compilar los ficheros ``.rst`` a HTML, se ejecuta ``sphinx-build`` **desde la carpeta ``@Documentacion\source``**.

- ``-b html``: Especifica el "builder" HTML.
- ``.``: Carpeta de origen (``@Documentacion\source``).
- ``_build``: Carpeta de destino para la salida HTML.

.. code-block:: powershell

   # Ruta completa al ejecutable de sphinx-build

    cd C:\Users\samue\Documents\dam2\DI-VARIOS_\Random\Sphinx\@Documentacion\source

y luego

    & "..\..\.venv\Scripts\sphinx-build.exe" -b html . _build
Este comando se ejecuta cada vez que actualizas la documentación o el código para regenerar el sitio HTML.
