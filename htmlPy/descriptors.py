class IntegralGeometricProperty(object):
    """ Descriptor for geometric properties of type intger for ``BaseGUI``.

    This descriptor should be used for width, height, X and Y attributes of
    ``QtMainWindow``. This should define properties of class
    :py:class:`htmlPy.BaseGUI` and the classes which inherit it. This retrieves
    the real values of the dimensions from the ``QtMainWindow`` when accessed
    and changes the real value when assigned. The values assigned should be of
    the type ``int``. Attributes defined by this descriptor cannot be deleted.

    Arguments:
        name (str): Name of the method of ``QMainWindow`` which refers to the
            corresponding property. Name should be amongst width, height, x
            and y, though others can be used if compatible.

    Attributes:
        name (str): Name of the method of ``QMainWindow`` which refers to the
            corresponding property. Name should be amongst width, height, x
            and y, though others can be used if compatible.

    """

    def __init__(self, name):
        """ Constructor for ``IntegralGeometricProperty`` class. """
        self.name = name

    def __get__(self, instance, cls):
        """ Getter for ``IntegralGeometricProperty`` descriptor.

        Returns the value of the property of ``instance`` which corresponds to
        the property defined by ``self``.

        Returns:
            int: Value of the property of instance.
        """
        real_value = getattr(instance.window, self.name)()
        setattr(instance, "_" + self.name, real_value)
        return real_value

    def __set__(self, instance, value):
        """ Setter for ``IntegralGeometricProperty`` descriptor.

        Sets the value of the property of ``instance`` which corresponds to
        the property defined by ``self``.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is negative.
        """

        if not isinstance(value, int):
            raise TypeError("Assignment type mismatch. " +
                            "{} should be an integer.".format(
                                self.name.title()))
        if value < 0:
            raise ValueError(self.name.title() + " should be >= 0.")
        setattr(instance, "_" + self.name, value)
        instance.auto_resize()

    def __delete__(self, instance):
        """ Deleter for ``IntegralGeometricProperty`` descriptor.

        The deleter raises error as property should not be deleted.

        Raises:
            AttributeError: The property should not be deleted.
        """

        raise AttributeError("The attribute can't be deleted.")


class CustomAssignmentProperty(object):
    """ Descriptor for some specific properties of :py:class:`htmlPy.BaseGUI`

    There are many properties of :py:class:`htmlPy.BaseGUI` objects which have
    following things in common. Their values are stored in a hidden class
    attribute which is returned when the properties are retrieved. And a small
    code has to be executed when setting their values. This descriptor is used
    to define those properties.

    Arguments:
        name (str): Name of the hidden class attribute to store value in
            without the leading "_"
        datatype (type): Type of the value of this property
        function (function): The function that has to be executed when
            assigning the value of this property.

    Attributes:
        name (str): Name of the hidden class attribute to store value in
            without the leading "_"
        type (type): Type of the value of this property
        assignment_function (function): The function that has to be executed
            when assigning the value of this property. If this function fails,
            the value will not be assigned.
    """

    def __init__(self, name, datatype, function):
        """ Constructor for ``CustomAssignmentProperty`` class """
        self.name = name
        self.type = datatype
        self.assignment_function = function

    def __get__(self, instance, cls):
        """ Getter for ``CustomAssignmentProperty`` descriptor

        Returns the value stored in the hidden class attribute.

        Returns:
            self.type: Returns the value of the property
        """
        return getattr(instance, "_" + self.name)

    def __set__(self, instance, value):
        """ Setter for ``CustomAssignmentProperty`` descriptor

        Executes ``self.assignment_function`` and sets the value in the hidden
        class attribute. If ``self.assignment_function`` function fails, the
        hidden class attribute will remain unchanged.

        Raises:
            TypeError: If value is not of self.type
            Exception: Any error raised by ``self.assignment_function``
        """

        if not isinstance(value, self.type):
            raise TypeError("Assignment type mismatch. " +
                            "{} should be of type {}.".format(
                                self.name.title(), self.type.__name__))
        self.assignment_function(instance, value)
        setattr(instance, "_" + self.name, value)

    def __delete__(self, instance):
        """ Deleter for ``CustomAssignmentProperty`` descriptor.

        The deleter raises error as property should not be deleted.

        Raises:
            AttributeError: The property should not be deleted.
        """

        raise AttributeError("The attribute can't be deleted.")


class LiveProperty(object):
    """ Descriptor for some specific properties of ``BaseGUI``

    There are many properties of :py:class:`htmlPy.BaseGUI` objects which have
    following things in common. They are some attributes of some of the Qt
    objects associated with the GUI. These can be change with or without
    htmlPy APIs. Thus, their values cannot be stored for future retrieval.
    The values are retrieved directly from the Qt objects. Thus, they require
    a retrieval and an assignment function.

    Arguments:
        datatype (type): Type of the value of this property
        get_function (function): The function that has to be executed for
            getting the value of this property.
        set_function (function): The function that has to be executed for
            setting the value of this property.

    Attributes:
        type (type): Type of the value of this property
        get_function (function): The function that has to be executed for
            getting the value of this property.
        set_function (function): The function that has to be executed for
            setting the value of this property.
    """

    def __init__(self, datatype, get_function, set_function):
        """ Constructor for ``LiveProperty`` class """
        self.type = datatype
        self.get_function = get_function
        self.set_function = set_function

    def __get__(self, instance, cls):
        """ Getter for ``LiveProperty`` descriptor

        Returns the value returned by ``get_function``.

        Returns:
            self.type: Returns the value of the property

        Raises:
            Exception: Any error raised by ``self.get_function``
        """
        return self.get_function(instance)

    def __set__(self, instance, value):
        """ Setter for ``LiveProperty`` descriptor

        Executes ``self.set_function`` and sets the value to the Qt objects as
            instructed by ``self.set_function``.

        Raises:
            TypeError: If value is not of self.type
            Exception: Any error raised by ``self.set_function``
        """

        if not isinstance(value, self.type):
            raise TypeError("Assignment type mismatch. " +
                            "Value should be of type {}.".format(
                                self.type.__name__))
        self.set_function(instance, value)

    def __delete__(self, instance):
        """ Deleter for ``CustomAssignmentProperty`` descriptor.

        The deleter raises error as property should not be deleted.

        Raises:
            AttributeError: The property should not be deleted.
        """

        raise AttributeError("The attribute can't be deleted.")
