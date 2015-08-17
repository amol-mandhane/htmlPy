from PySide import QtGui, QtWebKit
import abc
import sys
import descriptors


class BaseGUI(object):
    """ Abstract GUI class for creating apps using PySide's Qt and HTML.

    This class shouldn't be used directly. It serves as a parent to other
    GUI classes. Use :py:class:`htmlPy.AppGUI` and
    :py:class:`htmlPy.WebAppGUI` for developing applications.

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

    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, title=u"Application", width=800, height=600,
                 x_pos=10, y_pos=10, maximized=False,
                 plugins=False, developer_mode=False,
                 allow_overwrite=False):
        """ Abstract constructor for the :py:class:`htmlPy.BaseGUI` class """

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

        self._width = width
        self._height = height
        self._x = x_pos
        self._y = y_pos

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
        if not self.maximized:
            self.window.resize(self._width, self._height)
            self.window.move(self._x, self._y)

    width = descriptors.IntegralGeometricProperty("width")
    height = descriptors.IntegralGeometricProperty("height")
    x_pos = descriptors.IntegralGeometricProperty("x")
    y_pos = descriptors.IntegralGeometricProperty("y")

    maximized = descriptors.LiveProperty(
        bool,
        lambda instance: instance.window.isMaximized(),
        lambda instance, value: instance.window.showMaximized() if value else
        instance.window.showNormal() and instance.auto_resize())

    title = descriptors.LiveProperty(
        unicode,
        lambda instance: instance.window.windowTitle(),
        lambda instance, value: instance.window.setWindowTitle(value))

    plugins = descriptors.LiveProperty(
        bool,
        lambda instance: instance.web_app.settings().testAttribute(
            QtWebKit.QWebSettings.PluginsEnabled),
        lambda instance, value: instance.web_app.settings().setAttribute(
            QtWebKit.QWebSettings.PluginsEnabled, value))

    developer_mode = descriptors.LiveProperty(
        bool,
        lambda instance: instance.web_app.settings().testAttribute(
            QtWebKit.QWebSettings.DeveloperExtrasEnabled),
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

    def stop(self):
        """ Stops the application. Use only to bind with signals.

        The Qt application does not have to be manually stopped. Also, after
        starting the application is stuck in the execution loop and will not go
        further until it is stopped. Calling this function manually is
        redundant. This function exits only to be binded with QSignals to stop
        the application when that signal is emitted.
        """
        self.app.quit()

    def execute(self):
        """ Executes the application without ending the process on its end.

        DO NOT execute this process directly. Use only when
        :py:meth:`htmlPy.BaseGUI.stop` is connected to some signal.
        """
        self.app.exec_()
