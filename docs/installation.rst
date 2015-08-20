Installation
=============

Installing htmlPy
~~~~~~~~~~~~~~~~~~~~~

.. note::

    htmlPy is dependent on PySide_ which is not included in dependencies. Please refer the `installation instructions for PySide <pyside_installation_>`_.


You can install htmlPy with :command:`pip`::

    $ [sudo] pip install htmlPy

Or with :command:`easy_install`::

    $ [sudo] easy_install htmlPy

Or download the `compressed archive from PyPI <https://pypi.python.org/pypi/htmlPy/>`_, extract it, and inside it, run::

    $ [sudo] python setup.py install

.. note::
    Superuser access may be required if you are trying to install htmlPy globally. Please use **sudo** before the above commands in such case.


.. _pyside_installation:

Installing PySide_
~~~~~~~~~~~~~~~~~~~~

.. note::

    For detailed installation instructions, refer `PySide documentation <http://pyside.readthedocs.org/en/latest/index.html>`_.

htmlPy is dependent on PySide_ which is not included in the dependencies of htmlPy installation. PySide_ has to be installed manually. Following are the ways to do this.

1. On Windows
    PySide_ can be installed with :command:`pip`::

    $ pip install PySide

    Or with :command:`easy_install`::

    $ easy_install PySide

2. On Mac OS X

    You need to install or build Qt 4.8 first. You can use Homebrew and install Qt with::

    $ brew install qt

    After this, PySide_ can be installed with :command:`pip`::

    $ pip install PySide

    Or with :command:`easy_install`::

    $ easy_install PySide

2. On Linux (refer `this <http://pyside.readthedocs.org/en/latest/building/linux.html>`_ for detailed instructions)
    Installing PySide_ on linux with python installers is very slow as it requires compiling PySide_ from scratch. Hence, it is not included in the dependencies.

    A faster way is to use package managers of the operating system. On Ubuntu, you can install it with::

    $ sudo apt-get install python-pyside

    or::

    $ sudo apt-get install python3-pyside

    depending on the python version.

    If you are installing in a virtualenv or if you want to build PySide_ from scratch, you can install it with python installers. (This will take quite some time to compile)::

    $ [sudo] pip install PySide
    $ [sudo] easy_install PySide

    Or refer to `this <http://pyside.readthedocs.org/en/latest/building/linux.html>`_ link.

.. _PySide: http://pyside.org/
