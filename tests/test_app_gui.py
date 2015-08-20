from .base_gui_basics import BaseGUIBasics
from .base_gui_geometry import BaseGUIGeometry
from .base_gui_maximized_geometry import BaseGUIMaximizedGeometry
from .base_gui_live_properties import BaseGUILiveProperties
from .base_gui_javascript import BaseGUIJavascript
import htmlPy
import unittest
import os


class TestApp(unittest.TestCase, BaseGUIBasics,
              BaseGUIGeometry, BaseGUILiveProperties):

    def setUp(self):
        self.app = htmlPy.AppGUI(width=512, height=256, x_pos=32, y_pos=16,
                                 title=u"Test Title", allow_overwrite=True)
        self.AppClass = htmlPy.AppGUI

    def test_html(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  "template_and_static/index.html")) as f:
            html = htmlPy.unicode(f.read())
        self.app.html = html
        assert "Template Testing" in self.app.html


class TestAppGUITemplating(unittest.TestCase, BaseGUIJavascript):

    def setUp(self):
        self.app = htmlPy.AppGUI(allow_overwrite=True)
        self.app.static_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "template_and_static/")
        self.app.template_path = self.app.static_path
        self.reloader()

    def reloader(self):
        self.app.template = ("index.html", {"appname": "htmlPy Testing"})

    def test_template_loading(self):
        assert "Template Testing" in self.app.html

    def test_template_rendering(self):
        assert "htmlPy Testing" in self.app.html

    def test_staticfile_filter(self):
        assert "file:///" + \
            os.path.join(self.app.static_path, "script.js") in self.app.html


class TestAppJavascript(unittest.TestCase):  # , BaseGUIJavascript):

    def setUp(self):
        self.app = htmlPy.AppGUI(allow_overwrite=True)
        self.url = u"http://example.com/"
        self.app.web_app.loadFinished.connect(self.app.stop)
        self.app.url = self.url
        self.app.execute()


class TestAppMaximizedGeometry(unittest.TestCase, BaseGUIMaximizedGeometry):

    def setUp(self):
        self.app = htmlPy.AppGUI(maximized=True, allow_overwrite=True)


if __name__ == "__main__":
    unittest.main()
