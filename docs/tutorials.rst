Tutorials for common tasks
==========================
Following are some basic instructions for performing most common GUI and
Python tasks with htmlPy.

GUI to Python calls
~~~~~~~~~~~~~~~~~~~~~~~~
These calls work only for :py:class:`htmlPy.AppGUI` applications.

An essential aspect of GUI is to attach back-end calls to GUI events.
htmlPy needs the corresponding back-end functions to be selectively exposed
to GUI. The calls from GUI can be done in very HTML way.

The back-end functions that have to be attached to GUI events are
defined as follows

.. literalinclude:: codes/gui_to_python.py

After exposing the class methods to GUI, they can be called from HTML as
follows

.. literalinclude:: codes/gui_to_python.html
   :language: html


.. _py_to_gui:

Python to GUI calls
~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: codes/python_to_gui.py


General structure of htmlPy applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Following should be a general directory structure for htmlPy applications

.. code-block:: none

    back_end_codes/
    static/
        css/
            style.css
            .
            .
            .
        js/
            script.js
            .
            .
            .
        img/
            logo.img
            .
            .
            .
    templates/
        first_template_directory/
            template1.html
            template2.html
            .
            .
        another_template_directory/
            another_template.html
        base_layout.html
    main.py


``main.py`` is the driver file for the applications. In the driver file, you should initialize GUI, import functionalities from ``back_end_codes`` and bind it to GUI as explained on the first section of this page. Refer `this section <important.html>`_ for sample driver file.

In the ``back_end_codes``, you can import the ``app`` from ``main.py`` and perform operations on in as explained in `this section <py_to_gui_>`_.


Integration with django
~~~~~~~~~~~~~~~~~~~~~~~~~
Django can be used for standalone application development using htmlPy. The integration can be done easily. In the previous section, the django application and projects can be kept in ``back_end_codes`` directory. In the GUI driver file, include this code before initializing GUI for loading django settings.

.. code-block:: python

    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<project_name>.settings")


.. note::
    **TODO**: Add sample application developed using django and htmlPy

.. You can download a sample application created using django and htmlPy `here <http://amol-mandhane.github.io/htmlPy/django_sample.zip>`_.


Using file input
~~~~~~~~~~~~~~~~~
htmlPy replaces the HTML file input code with PyQt's file dialog. To use file input, write the file input tag with an additional data attribute for filtering extensions, if required. The filter attribute string should be of the form ``"[{'title': 'title for extension', 'extensions': 'space separated extensions'}, {'title': 'title for another extension', 'extensions': 'space separated extensions'}]"``. For example

.. code-block:: html

    <input type="file" name="file" id="file" data-filter="[{'title': 'Images', 'extensions': '*.png *.xpm *.jpg'}, {'title': 'Documents', 'extensions': '*.pdf *.doc *.docx'}]">

The json returned to the python backend for the form will have the absolute path of the selected file as the input value.
