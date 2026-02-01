.. _tutorial:

Tutorial Básico de reStructuredText
===================================

Sphinx utiliza reStructuredText (reST) como su lenguaje de marcado principal. Aquí tienes una guía rápida de sus elementos más comunes.

Títulos
-------

Se crean subrayando el texto. La longitud del subrayado debe coincidir con la del texto para que sea válido.

Nivel 1: `==========`
Nivel 2: `----------`
Nivel 3: `~~~~~~~~~~`

Estilos de Texto
----------------

-   **Texto en negrita**: ``**Texto en negrita**``
-   *Texto en cursiva*: ``*Texto en cursiva*``
-   `Código monoespaciado`: `` `Código monoespaciado` ``

Listas
------

Listas no ordenadas:

*   Elemento 1
*   Elemento 2
    *   Sub-elemento 2.1
    *   Sub-elemento 2.2

Listas ordenadas:

1.  Primer paso
2.  Segundo paso
3.  Tercer paso

Bloques de Código
-----------------

Para mostrar bloques de código, se usa la directiva `.. code-block::` seguida del lenguaje.

.. code-block:: python

   def mi_funcion(parametro):
       print(f"Procesando: {parametro}")
       return True

Enlaces
-------

Los enlaces permiten navegar entre documentos o ir a recursos externos.

-   **Enlace interno**: Se usa `:doc:` seguido del nombre del archivo `.rst` (sin extensión). Por ejemplo, para enlazar a `api_reference.rst` se escribe :doc:`api_reference`.
-   **Enlace externo**: Se usa ``Texto del enlace <URL>``_. El guion bajo al final es necesario. Por ejemplo: `Documentación oficial de Sphinx <https://www.sphinx-doc.org/>`_.
