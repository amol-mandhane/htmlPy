from .base_gui_basics import BaseGUIBasics
from .base_gui_geometry import BaseGUIGeometry
from .base_gui_maximized_geometry import BaseGUIMaximizedGeometry
from .base_gui_live_properties import BaseGUILiveProperties
from .base_gui_javascript import BaseGUIJavascript
from .utilities import descriptor_check
import htmlPy
import unittest


class TestWebApp(unittest.TestCase, BaseGUIBasics,
                 BaseGUIGeometry, BaseGUILiveProperties):

    def setUp(self):
        self.app = htmlPy.WebAppGUI(width=512, height=256, x_pos=32, y_pos=16,
                                    title=u"Test Title", allow_overwrite=True)
        self.AppClass = htmlPy.WebAppGUI
        self.url = u"http://example.com/"

    test_url_type = descriptor_check("url", "non-unicode", TypeError)

    def test_url_setting(self):
        self.app.url = self.url
        assert self.app.url == self.url

    def test_url_loading(self):
        self.app.web_app.loadFinished.connect(self.app.stop)
        self.app.url = self.url
        self.app.execute()
        assert u"Example Domain" in self.app.html


class TestWebAppJavascript(unittest.TestCase, BaseGUIJavascript):

    def setUp(self):
        self.app = htmlPy.WebAppGUI(allow_overwrite=True)
        self.reloader()

    def reloader(self):
        self.url = u"http://example.com/"
        self.app.web_app.loadFinished.connect(self.app.stop)
        self.app.url = self.url
        self.app.execute()


class TestWebAppMaximizedGeometry(unittest.TestCase, BaseGUIMaximizedGeometry):

    def setUp(self):
        self.app = htmlPy.WebAppGUI(maximized=True, allow_overwrite=True)


if __name__ == "__main__":
    unittest.main()
