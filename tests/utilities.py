def descriptor_check(attribute, value, error):

    def checker(instance):
        try:
            setattr(instance, attribute, value)
        except error:
            pass
        except Exception as e:
            raise e
        else:
            raise AssertionError('Descriptor failed')

    return checker


def html_with_string(s):
    return "<html><head></head><body>{}</body></html>".format(s)
