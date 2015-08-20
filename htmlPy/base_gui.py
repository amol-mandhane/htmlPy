from PySide import QtGui, QtWebKit
from . import settings, descriptors, unicode
import abc
import sys


RIGHT_CLICK_SETTING_KEY = "RIGHT_CLICK"
RIGHT_CLICK_ENABLE = "document.oncontextmenu = null;"
RIGHT_CLICK_DISABLE = "document.oncontextmenu = function(e) { return false; };"
RIGHT_CLICK_INPUTS_ONLY = "document.oncontextmenu = function(e) {" + \
    "return e.target.nodeName == 'INPUT' || e.target.nodeName == 'TEXTAREA'};"

TEXT_SELECTION_SETTING_KEY = "TEXT_SELECTION"
TEXT_SELECTION_ENABLE = "document.onselectstart = null;" + \
    "document.body.style.webkitUserSelect = '';" + \
    "document.body.style.cursor = '';"
TEXT_SELECTION_DISABLE = "document.onselectstart = function(e) " + \
    "{ return false; }; document.body.style.webkitUserSelect = 'none';" + \
    "document.body.style.cursor = 'default';"


class BaseGUI(object):
    """ Abstract GUI class for creating apps using PySide's Qt and HTML.

    This class shouldn't be used directly. It serves as a parent to other
    GUI classes. Use :py:class:`htmlPy.AppGUI` and
    :py:class:`htmlPy.WebAppGUI` for developing applications.

    Arguments:
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

        self._javascript_settings = {}
        self.web_app.loadFinished.connect(self.__javascript_setting_call)

        self._width = width
        self._height = height
        self._x = x_pos
        self._y = y_pos

        self.title = title
        self.plugins = plugins
        self.developer_mode = developer_mode

        self.maximized = maximized
        self.auto_resize()

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
            QtWebKit.QWebSettings.WebAttribute.DeveloperExtrasEnabled),
        lambda instance, value: instance.web_app.settings().setAttribute(
            QtWebKit.QWebSettings.WebAttribute.DeveloperExtrasEnabled, value))

    def __javascript_setting_call(self):
        """ Re-evaluate javascript settings

        This function re-evaluates all the javascript settings defined in the
        dictionary ``_javascript_settings``. This should be connected
        to the slot ``web_app.loadFinished``.
        """
        javascript_string = ";".join(self._javascript_settings.values())
        if len(javascript_string) > 0:
            self.evaluate_javascript(javascript_string)

    def auto_resize(self):
        """ Resizes and relocates the ``window`` to previous state

        If the ``window`` is not maximized, this function resizes it to the
        stored dimensions, moves it to the stored location.
        """
        if not self.maximized:
            self.window.resize(self._width, self._height)
            self.window.move(self._x, self._y)

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

    def evaluate_javascript(self, javascript_string):
        """ Evaluates javascript in web page currently displayed

        Arguments:
            javascript_string (str): The string of javascript code that has to
                be evaluated.
        """
        self.web_app.page().mainFrame().evaluateJavaScript(javascript_string)

    def right_click_setting(self, value):
        """ Javascript based setting for right click on the application.

        This function changes the web page's behaviour on right click. Normal
        behaviour is to open a context menu. Enabling right click exhibits that
        behaviour. Right click is enabled by default. Disabling right click
        suppresses context menu for entire page. Enabling right click for
        only inputs suppresses context menu for all elements excepts inputs and
        textarea, which is the recommended option. The arguments provided
        should be from :py:mod:`htmlPy.settings` module as explained further.

        Arguments:
            value (int): should be either ``htmlPy.settings.ENABLE`` (default)
                or ``htmlPy.settings.DISABLE`` or
                ``htmlPy.settings.INPUTS_ONLY`` (recommended)

        """
        if value == settings.ENABLE:
            self.evaluate_javascript(RIGHT_CLICK_ENABLE)
            self._javascript_settings.pop(RIGHT_CLICK_SETTING_KEY, None)
        elif value == settings.DISABLE:
            self.evaluate_javascript(RIGHT_CLICK_DISABLE)
            self._javascript_settings[RIGHT_CLICK_SETTING_KEY] = \
                RIGHT_CLICK_DISABLE
        elif value == settings.INPUTS_ONLY:
            self.evaluate_javascript(RIGHT_CLICK_INPUTS_ONLY)
            self._javascript_settings[RIGHT_CLICK_SETTING_KEY] = \
                RIGHT_CLICK_INPUTS_ONLY
        else:
            raise ValueError("The argument should be either " +
                             "htmlPy.settings.ENABLE or " +
                             "htmlPy.settings.DISABLE or " +
                             "htmlPy.settings.INPUTS_ONLY")

    def text_selection_setting(self, value):
        """ Javascript based setting for text selection in the application.

        This function changes the web page's behaviour on selection of text.
        Normal behaviour is to highlight the selected text. Enabling text
        selection exhibits that behaviour. Text selection is enabled by
        default. Disabling text selection disallows user to select any text on
        the page except for inputs and disables the I-beam cursor for text
        selection. The arguments provided should be from
        :py:mod:`htmlPy.settings` module as explained further.

        Arguments:
            value (int): should be either ``htmlPy.settings.ENABLE`` (default)
                or ``htmlPy.settings.DISABLE`` or

        """

        if value == settings.ENABLE:
            self.evaluate_javascript(TEXT_SELECTION_ENABLE)
            self._javascript_settings.pop(TEXT_SELECTION_SETTING_KEY, None)
        elif value == settings.DISABLE:
            self.evaluate_javascript(TEXT_SELECTION_DISABLE)
            self._javascript_settings[TEXT_SELECTION_SETTING_KEY] = \
                TEXT_SELECTION_DISABLE
        else:
            raise ValueError("The argument should be either " +
                             "htmlPy.settings.ENABLE or " +
                             "htmlPy.settings.DISABLE")
