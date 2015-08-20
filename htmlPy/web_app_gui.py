from .base_gui import BaseGUI
from . import descriptors, unicode


class WebAppGUI(BaseGUI):
    """ GUI class for creating web apps using PySide's Qt.

    The class WebAppGUI can be used to create web based applications in a
    QtWebKit based browser running on user side. The server for the web app
    can be remote or local. This can be used for quick desktop deployment of
    existing websites. However, for a standalone application, it is recommended
    to used :py:class:`htmlPy.AppGUI` class.

    Note:
        Arguments and Attributes of this class come from the parent class
        :py:class:`htmlPy.BaseGUI`. Please refer to its documentation for more
        details.

    Keyword arguments:
        title (Optional[unicode]): The title of the ``window``. Defaults to
            u"Application".
        width (Optional[int]): Width of the ``window`` in pixels. Defaults to
            800 px. Redundant if ``maximized`` is ``True``.
        height (Optional[int]): Height of the ``window`` in pixels. Defaults to
            600 px. Redundant if ``maximized`` is ``True``.
        x_pos (Optional[int]): The X-coordinate for top-left corner of the
            ``window`` in pixels. Defaults to 10 px. Redundant if
            ``maximized`` is ``True``.
        y_pos (Optional[int]): The Y-coordinate for top-left corner of the
            ``window`` in pixels. Defaults to 10 px. Redundant if
            ``maximized`` is ``True``.
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
        url (unicode property): The URL currently being displayed in
            ``window``. Set the property to a URL unicode string to change the
            URL being displayed.
        html (unicode property): The HTML currently rendered in the
            ``web_app``. This is a readonly property.
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
        super(WebAppGUI, self).__init__(*args, **kwargs)

    url = descriptors.LiveProperty(
        unicode,
        lambda instance: instance.web_app.url().toString(),
        lambda instance, link: instance.web_app.setUrl(link))

    @property
    def html(self):
        """ unicode: The HTML currently rendered in the window.

        This property will return the HTML which is being displayed in the
        ``web_app``. This is not asynchronous. The URL set with htmlPy will not
        load until the window is in display.
        """

        return self.web_app.page().mainFrame().toHtml()
