from base_gui import BaseGUI
import descriptors
import os
import jinja2


class AppGUI(BaseGUI):
    """ GUI class for creating apps using PySide's QtWebkit.

    The class AppGUI can be used to create standalone applications with HTML
    GUI. It uses Jinja2 templating engine for generating HTML which can be
    overridden.

    Note: Arguments and Attributes of this class come from the parent class
        :py:class:`htmlPy.BaseGUI`. Please refer to it's documentation for more
        details.

    Keyword arguments:
        title (Optional[unicode]): The title of the ``window``. Defaults to
            u"Application".
        width (Optional[int]): Width of the ``window`` in pixels. Defaults to
            800 px. Redundant if ``maximized`` is ``True``.
        height (Optional[int]): Height of the ``window`` in pixels. Defaults to
            600 px. Redundant if ``maximized is ``True``.
        x_pos (Optional[int]): The X-coordinate for top-left corner of the
            ``window`` in pixels. Defaults to 10 px. Redundant if
            ``maximized is ``True``.
        y_pos (Optional[int]): The Y-coordinate for top-left corner of the
            ``window`` in pixels. Defaults to 10 px. Redundant if
            ``maximized is ``True``.
        maximized (Optional[bool]): ``window`` is maximized when set to
            ``True``. Defaults to ``False``.
        plugins (Optional[bool]): Enables plugins like flash when set as
            ``True``. Defaults to ``False``.
        developer_mode (Optional[bool]): Enables developer mode when set as
            ``True``. Defaults to ``False``. The developer mode gives access
            to web inspector and other development tools and enables
            right-click on the webpage.
        allow_overwrite (Optional[bool]): ``PySide.QtGui.QApplication`` can be
            instantiated only once. If it is already instantiated, then setting
            ``allow_overwrite`` to ``True`` overwrites the ``QApplication``'s
            window with window of this class instance. If ``False``,
            RuntimeError is raised. If ``QApplication`` is not instantiated,
            this is irrelevent.


    Attributes:
        app (PySide.QtGui.QApplication): The singleton Qt application object.
            This can be instantiated only once in the entire process.
        window (PySide.QtGui.QMainWindow): The window being displayed in the
            ``app``.
        web_app (PySide.QtWebKit.QWebView): The web view widget which renders
            and displays HTML in the a ``window``.
        html (unicode property): The HTML currently rendered in the
            ``web_app``. The HTML in ``web_app`` can be changed by assigning
            the new HTML to this property.
        static_path (str property): The absolute path relative to which the
            ``staticfile`` filter will create links in templating. Changing
            this creates a function dynamically which replaces current
            ``staticfile`` filter in current templating environment.
        template_path (str property): The absolute path relative to which
            jinja2 finds the templates to be rendered. Changing this updates
            the template loader in current templating environment.
        template (tuple(str, dict) property): The current template being
            displayed in ``web_app``. First element of the tuple is the
            path of the template file relative to ``template_path``. The
            second element of the tuple is the context dictionary in which it
            is being rendered.
        maximized (bool property): A boolean which describes whether the
            ``window`` is maximized or not. Can be set to ``True`` to maximize
            the window and set to ``False`` to restore.
        width (int property): Width of the ``window`` in pixels. Set the value
            of this property in pixels to change the width.
        height (int property): Height of the ``window`` in pixels. Set the
            value of this property in pixels to change the height.
        x_pos (int property): The X-coordinate for top-left corner of the
            ``window`` in pixels. Set the value of this property in pixels to
            move the ``window`` horizontally.
        y_pos (int property): The Y-coordinate for top-left corner of the
            ``window`` in pixels. Set the value of this property in pixels to
            move the ``window`` vertically.
        title (unicode property): The title of the ``window``. Set the value of
            this property to change the title.
        plugins (bool property): A boolean flag which indicates whether plugins
            like flash are enabled or not. Set the value to ``True`` or
            ``False`` as required.
        developer_mode (bool property): A boolean flag which indicated whether
            developer mode is active or not. The developer mode gives access
            to web inspector and other development tools and enables
            right-click on the webpage. Set the value to ``True`` or ``False``
            as required.

    Raises:
        RuntimeError: If ``PySide.QtGui.QApplication`` is already instantiated
            and ``allow_overwrite`` is ``False``.

    """

    def __init__(self, *args, **kwargs):
        """ Constructor for :py:class:`htmlPy.WebAppGUI` class """
        super(AppGUI, self).__init__(*args, **kwargs)

        self.__driver_script_location = os.path.abspath(
            os.path.dirname(__file__))

        self.__templating_environment = jinja2.Environment()
        self.static_path = self.__driver_script_location
        self.template_path = self.__driver_script_location

    html = descriptors.LiveProperty(
        unicode,
        lambda instance: instance.web_app.page().mainFrame().toHtml(),
        lambda instance, value: instance.web_app.setHtml(value))

    static_path = descriptors.CustomAssignmentProperty(
        "static_path", str,
        lambda instance, value: instance._change_static_path(value))

    template_path = descriptors.CustomAssignmentProperty(
        "template_path", str,
        lambda instance, value: instance._change_template_path(value))

    @property
    def template(self):
        """
        tuple(str, dict): The current template being displayed in ``web_app``.
            First element of the tuple is the path of the template file
            relative to ``template_path``. The second element of the tuple is
            the context dictionary in which it is being rendered.
        """
        return self.__template

    @template.setter
    def template(self, template_tuple):
        """ Display the template represented by ``template_tuple``

        This function renders the template represented by ``template_tuple``
        using jinja2 and sets the result as the HTML of current ``web_app``.
        """
        if not isinstance(template_tuple, tuple):
            raise TypeError("A tuple is required")
        template_path, context = template_tuple
        if not isinstance(template_path, str):
            raise TypeError("Template path should be a string")
        if not isinstance(context, dict):
            raise TypeError("Context should be a dictionary")

        template = self.__templating_environment.get_template(template_path)
        self.html = template.render(**context)
        self.__template = template_tuple

    def _change_static_path(self, value):
        """ Changes the static_path for jinja2 filters

        NEVER EVER call this function. It is meant for internal use only.
        """
        def staticfile_filter(file_path):
            return "file:///" + os.path.join(value, file_path)

        self.__templating_environment.filters["staticfile"] = staticfile_filter

    def _change_template_path(self, value):
        """ Changes the template_path for jinja2 environment

        NEVER EVER call this function. It is meant for internal use only.
        """
        self.__templating_enviroment.loader = jinja2.FileSystemLoader(value)
