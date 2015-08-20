from .utilities import descriptor_check


class BaseGUILiveProperties(object):

    test_title_type = descriptor_check("title", "non-unicode", TypeError)
    test_developer_mode_type = descriptor_check("developer_mode", 1, TypeError)
    test_plugins_type = descriptor_check("plugins", 1, TypeError)

    def test_title(self):
        assert self.app.title == u"Test Title"

    def test_title_setting(self):
        self.app.title = u"Modified Title"
        assert self.app.title == u"Modified Title"

    def test_developer_mode(self):
        assert not self.app.developer_mode

    def test_developer_mode_setting(self):
        self.app.developer_mode = True
        assert self.app.developer_mode

    def test_plugins(self):
        assert not self.app.plugins

    def test_plugins_setting(self):
        self.app.plugins = True
        assert self.app.plugins
