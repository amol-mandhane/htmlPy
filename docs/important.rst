Important instructions for application development with htmlPy
=================================================================

.. _driver_file:

Use a driver file
~~~~~~~~~~~~~~~~~~~~

Keep your application modularized. Use a separate file for initialization,
configuration and execution of htmlPy GUI. Do not include any back-end
functionalities in this file. The driver file structure should be

1. Initial configurations
2. htmlPy GUI initialization
3. htmlPy GUI configuration
4. Binding of back-end functionalities with GUI
    a. Import back-end functionalities
    b. Bind imported functionalities
5. Instructions for running front-end in ``if __name__ == "__main__":`` conditional. **Always keep the GUI starter code in the ``if __name__ == "__main__":`` conditional**. The GUI has to be started only when the driver file is running, not when it is being imported

Here's a sample driver file

.. literalinclude:: codes/driver.py


Set ``static_path`` and ``template_path``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When using :py:class:`htmlPy.AppGUI`, always set ``static_path`` and ``template_path`` right after instantiating GUI. Set ``BASE_DIR`` variable as the absolute path to the directory of the driver file and set ``static_path`` and ``template_path`` with respect to ``BASE_DIR``. Refer to the `driver file section <driver_file_>`_ for example.

htmlPy uses `Jinja2 <http://jinja.pocoo.org/>`_ for templating which is inspired by Django's templating system but extends with powerful tools. Jinja2 requires a base directory to be set. This can be done by setting the ``template_path`` as displayed in `driver file section <driver_file_>`_. You can use your own templating system as :py:class:`htmlPy.AppGUI` allows setting the attribute ``html``.

``static_path`` is where all the static files including images, stylesheets and javascripts are stored. The static files will have to be present on the user computer and using htmlPy static filter, their links can be generated dynamically. For example,

.. code-block:: html

    <script src="{{ 'js/jquery.min.js'|staticfile }}"></script>
    <link rel="stylesheet" href="{{ 'css/bootstrap.min.css'|staticfile }}">
