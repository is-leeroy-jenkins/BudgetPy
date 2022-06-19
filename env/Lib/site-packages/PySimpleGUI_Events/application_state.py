class SimpleApplicationState(object):
    def __init__(self, window, **kwargs):
        self.window = window
        self.state = kwargs

    def __getitem__(self, item):
        return self.state[item]

    def __setitem__(self, key, value):
        self.state[key] = value

    def __delitem__(self, key):
        del self.state[key]
