def descriptor_check(attribute, value, error):

    def checker(instance):
        try:
            setattr(instance, attribute, value)
        except error:
            pass
        except Exception, e:
            raise e
        else:
            raise AssertionError('Descriptor failed')

    return checker
