from .application_state import SimpleApplicationState
from .handler import SimpleHandler, Abort


class EventManager(object):
    def __init__(self):
        """Create a new EventManager object with an empty handler dictionary."""
        self.handlers = dict()

    def __getitem__(self, key):
        """Get all handler functions for a given key."""
        return self.handlers[key]

    def __iadd__(self, other: SimpleHandler):
        """Add an event handler to the Manager."""
        if type(other) != SimpleHandler:
            raise Exception("Attempted to add a non-SimpleHandler handler")

        if other.key not in self.handlers:
            self.handlers[other.key] = list()
        self.handlers[other.key].append(other.handler_function)

        return self

    def execute(self, key, data, application_state=None):
        """Execute all handler functions for a given key with the passed data on the passed application_state.
        The passed key string is the key string passed back from SimpleGUI's window.read()
        The passed data object is the dictionary passed back from SimpleGUI's window.read()
        The passed application_state needs to be an ApplicationState object with a window object
        that handlers can use to change the GUI.
        """
        if not issubclass(type(application_state), SimpleApplicationState):
            raise Exception("Expected a SimpleApplicationState object.")

        for handler in self.handlers[key]:
            try:
                handler(data, application_state)
            except Abort:
                break

        return application_state
