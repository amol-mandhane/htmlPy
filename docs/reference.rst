API Reference
=============

Class :py:class:`htmlPy.AppGUI` (:py:class:`htmlPy.BaseGUI`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: htmlPy.AppGUI
    :members:
    :inherited-members:


Class :py:class:`htmlPy.WebAppGUI` (:py:class:`htmlPy.BaseGUI`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: htmlPy.WebAppGUI
    :members:
    :inherited-members:

Class :py:class:`htmlPy.Object`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. py:class:: htmlPy.Object

    Alias of ``PySide.QtCore.QObject``.

    For binding python functionalities to GUI, the classes being bound should
    inherit :py:class:`htmlPy.Object`. Its constructor has to be called. The methods
    of the class that have to be bound to GUI must be decorated with
    :py:class:`htmlPy.Slot`.

    Example:
        Refer to the API reference of :py:class:`htmlPy.Slot` for an example.


Decorator :py:class:`htmlPy.Slot`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. py:class:: htmlPy.Slot

    Alias of ``PySide.QtCore.Slot``

    This decorator binds the methods of classes which inherit :py:class:`htmlPy.Object`
    to the GUI. The argument types and return type of the method being bound have
    to be provided as argument to the decorator.

    :param [type] *args: Data types of arguments of the method being decorated
    :keyword type result: Data type of return value of the method being decorated

    Example:
        .. code-block:: python

            import htmlPy
            htmlPy_app = htmlPy.AppGUI()


            class BindingClass(htmlPy.Object):

                @htmlPy.Slot(str, int, result=int)
                def binding_method(self, string_arg, int_arg):
                    int_return = 1
                    return int_return

            htmlPy_app.bind(BindingClass())


Module :py:mod:`htmlPy.settings`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: htmlPy.settings

Class :py:class:`htmlPy.BaseGUI`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: htmlPy.BaseGUI
    :members:
