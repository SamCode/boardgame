# event-based architecture

# problem: 
# if view doesn't get notified of events, it will have to
# recalculate everything every iteration of view.update()

# problem:
# if every Model is notified of every Event, function calls will be wasted
# on Model objects that don't care about certain Events.

class Event(object):
    """A potential change in program state, created by a Controller."""

    def __init__(self):
        """Initialize this type of event with required parameters."""

class Program(object):
    """Runs the program."""

    def __init__(self):
        self._models = []
        self._views = []
        self._controllers = []

    def run(self):
        while True:
            for controller in self._controllers:
                for event in controller.detect():
                    for model in self._models:
                        model.process(event)
                    for view in self._views:
                        view.process(event)
            for view in self._views:
                view.update(self._models)

class Model(object):
    """State representing functionality of a program in terms of 
    responses to Event objects."""

    def __init__(self):
        """Initialize object state."""

    def process(self, event):
        """Update self's object state."""
        # super(Model, self).process(event)

class View(object):
    """An external representation of program state."""

    def __init__(self):
        """Initialize variables to store intermediary data required to
        display program state."""

    def update(self, models):
        """..."""

    def process(self, models):
        """..."""

class Controller(object):
    """An external influence on program state, via Event objects."""

    def __init__(self):
        """Initialize controller state."""

    def detect(self):
        """Returns a list of Event objects."""