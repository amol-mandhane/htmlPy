class BaseGUIMaximizedGeometry(object):

    def test_window_maximized(self):
        assert self.app.maximized

    def test_can_minimize(self):
        self.app.maximized = False
        assert not self.app.maximized
