from PySide import QtGui, QtWebKit
import abc
import sys
import descriptors


class BaseGUI(object):
    """ Abstract GUI class for creating apps using PySide's Qt and HTML.

    This class shouldn't be used directly. It serves as a parent to other
    GUI classes. Use :py:mod:`htmlPy.AppGUI` and
    :py:mod:`htmlPy.WebAppGUI` for developing applications.

    Args:
        No args: This is an abstract base class. It must not be instantiated.

    Attributes:
        app (PySide.QtGui.QApplication): The singleton Qt application object.
            This can be instantiated only once in the entire process.
        window (PySide.QtGui.QMainWindow): The window being displayed in the
            ``app``.
        web_app (PySide.QtWebKit.QWebView): The web view widget which renders
            and displays HTML in the a ``window``.
        maximized (bool property): A boolean which describes whether the
            app is maximized or not. Can be set to ``True`` to maximize the
            app and set to ``False`` to restore.
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
        title (str property): The title of the ``window``. Set the value of
            this property to change the title.
        plugins (bool property): A boolean flag which indicates whether plugins
            like flash are enabled or not. Set the value to ``True`` or
            ``False`` as required.
        developer_mode (bool property): A boolean flag which indicated whether
            developer mode is active or not. The developer mode gives access
            to web inspector and other development tools and enables
            right-click on the webpage. Set the value to ``True`` or ``False``
            as required.

    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, title="Application", width=800, height=600,
                 x_pos=10, y_pos=10, maximized=False,
                 plugins=False, developer_mode=False,
                 allow_overwrite=False):
        """ An abstract constructor for the :py:mod:`htmlPy.BaseGUI` class """

        app = QtGui.QApplication.instance()
        if app is not None and not allow_overwrite:
            raise RuntimeError("Another htmlPy application is already running")
        elif app is not None:
            self.app = app
        else:
            self.app = QtGui.QApplication(sys.argv)

        self.web_app = QtWebKit.QWebView()
        self.window = QtGui.QMainWindow()
        self.window.setCentralWidget(self.web_app)
        self.web_app.settings().setAttribute(
            QtWebKit.QWebSettings.LocalContentCanAccessRemoteUrls, True)

        self.__maximized = None
        self.__width = width
        self.__height = height
        self.__x = x_pos
        self.__y = y_pos

        self.__title = None
        self.__plugins = None
        self.__developer_mode = None

        self.title = title
        self.plugins = plugins
        self.developer_mode = developer_mode

        self.maximized = maximized
        self.auto_resize()

    def auto_resize(self):
        """ Resizes and relocates the ``window`` to previous state

        If the ``window`` is not maximized, this function resizes it to the
        stored dimensions, moves it to the stored location.
        """
        if not self.__maximized:
            self.window.resize(self.__width, self.__height)
            self.window.move(self.__x, self.__y)

    @property
    def maximized(self):
        """bool: A flag which indicates whether the ``window`` is maximized or
        not.
        """
        self.__maximized = self.window.isMaximized()
        return self.__maximized

    @maximized.setter
    def maximized(self, value):
        """ Maximizes or restores the ``window`` based on the value provided.

        Raises:
            TypeError: if the value provided is not boolean.
        """
        if not isinstance(value, bool):
            raise TypeError("Assignment type mismatch. " +
                            "maximized should be bool.")
        self.__maximized = value
        if self.__maximized:
            self.window.showMaximized()
        else:
            self.window.showNormal()
            self.auto_resize()

    width = descriptors.IntegralGeometricProperty("width")
    height = descriptors.IntegralGeometricProperty("height")
    x_pos = descriptors.IntegralGeometricProperty("x")
    y_pos = descriptors.IntegralGeometricProperty("y")

    title = descriptors.CustomAssignmentProperty(
        "title", str,
        lambda instance, value: instance.window.setWindowTitle(value))

    plugins = descriptors.CustomAssignmentProperty(
        "plugins", bool,
        lambda instance, value: instance.web_app.settings().setAttribute(
            QtWebKit.QWebSettings.PluginsEnabled, value))

    developer_mode = descriptors.CustomAssignmentProperty(
        "developer_mode", bool,
        lambda instance, value: instance.web_app.settings().setAttribute(
            QtWebKit.QWebSettings.DeveloperExtrasEnabled, value))

    def start(self):
        """ Starts the application.

        This is not asynchronous. Starting the application will halt the
        further processes. DO NOT start outside the
        ``if __name__ == "__main__":`` conditional
        """
        self.window.show()
        sys.exit(self.app.exec_())
