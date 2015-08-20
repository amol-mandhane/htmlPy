from .utilities import descriptor_check


class BaseGUIGeometry(object):

    test_width_type = descriptor_check("width", "non-int", TypeError)
    test_width_positive = descriptor_check("width", -1, ValueError)
    test_height_type = descriptor_check("height", "non-int", TypeError)
    test_height_positive = descriptor_check("height", -1, ValueError)
    test_x_pos_type = descriptor_check("x_pos", "non-int", TypeError)
    test_x_pos_positive = descriptor_check("x_pos", -1, ValueError)
    test_y_pos_type = descriptor_check("y_pos", "non-int", TypeError)
    test_y_pos_positive = descriptor_check("y_pos", -1, ValueError)

    test_maximized_type = descriptor_check("maximized", 1, TypeError)

    def test_default_width(self):
        assert self.app.width == 512

    def test_width_setting(self):
        self.app.width = 256
        assert self.app.width == 256

    def test_default_height(self):
        assert self.app.height == 256

    def test_height_setting(self):
        self.app.height = 128
        assert self.app.height == 128

    def test_default_x_pos(self):
        assert self.app.x_pos == 32

    def test_x_pos_setting(self):
        self.app.x_pos = 16
        assert self.app.x_pos == 16

    def test_default_y_pos(self):
        assert self.app.y_pos == 16

    def test_y_pos_setting(self):
        self.app.y_pos = 32
        assert self.app.y_pos == 32

    def test_not_maximized(self):
        assert not self.app.maximized

    def test_can_maximize(self):
        self.app.maximized = True
        assert self.app.maximized
