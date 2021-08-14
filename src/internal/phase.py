
from enum import Enum
from itertools import cycle

class Phase(Enum):
    DAY = 1
    NIGHT = 2
    # midnight, noon

class PhaseCycler:

    def __init__(self):
        self.__phases = cycle(Phase)

    def next(self):
        return next(self.__phases)