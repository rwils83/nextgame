from itertools import count
import weakref

class map(object):

    def __init__(self):
        pass


    def SaveMap(self):
        pass

    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead

class room(object):
    _ids = count(0)

    def __init__(self):
        self.id = next(self._ids)


class startingRoom(room):
    def __init__ (self):
        super().__init__()
