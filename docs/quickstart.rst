Quickstart tutorial of htmlPy
=============================

Standalone application
~~~~~~~~~~~~~~~~~~~~~~
Following code assumes that there is a file ``index.html`` in the same directory as the file and the script is being executed fromt the same directory.

.. literalinclude:: codes/sample_app.py


The above code instantiates an application, renders ``index.html`` file in that application using `Jinja2 templating engine <http://jinja.pocoo.org/>`_ and starts it.

Web based application
~~~~~~~~~~~~~~~~~~~~~
Following code is a web-based application displaying Python website. You can change the URL to a local or network server to display any website as an application.

.. literalinclude:: codes/sample_web_app.py
