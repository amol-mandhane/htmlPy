class BaseGUIBasics(object):

    def test_multiple_instance_error(self):
        try:
            self.AppClass()
        except RuntimeError:
            pass
        except Exception as e:
            raise e
        else:
            raise AssertionError("Test failed")
