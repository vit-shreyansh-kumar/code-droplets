
""" Obervable or Subject  -> NOTIFIES -> Observers """
""" Here Observers doesnot poll for the state of the Observable/Subject rather than that the Observable pushes the notification to the Observers about its state change. """
""" It defines the One to Many Relationship between the objects. """


class Observable:
    """ Represents what is being Observed. """

    def __init__(self):

        self._observers = list()

    def register(self, observer):

        if observer not in self._observers:
            self._observers.append(observer)

    def remove(self, observer):
        pass

    def notify(self, observer):
        pass

class Observer:

    def update(self):
        pass



