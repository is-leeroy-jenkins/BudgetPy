class SimpleHandler(object):
    """Create a SimpleHandler object that adds a handler function to the manager.

    Handler functions should satisfy the following function signature:
        def function(PySimpleGuiData, SimpleApplicationState)
    """

    def __init__(self, key, handler_function):
        self.key = key
        self.handler_function = handler_function
        self.aborted = False


class Abort(Exception):
    pass
