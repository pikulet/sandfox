from collections import defaultdict
from enum import Enum
from typing import List, NewType

from actions import *

class Alignment(Enum):
    TOWN = 1
    MAFIA = 2
    THIRD_PARTY = 3
    
class Role(NamedEntity):

    def __init__(self, name: str, alignment: Alignment):
        super().__init__(name)
        self.__alignment = alignment
        self.__actions = defaultdict(lambda: List[Action])
        self.__actions[Phase.DAY] = DayEliminationVote

    def get_alignment(self):
        return self.__alignment

    def get_actions(self, phase: Phase) -> List[Action]:
        return self.__actions[phase]

    def add_action(self, phase: Phase, action: Action):
        self.__actions[phase].append(action)

class Villager(Role):
    def __init__(self):
        super().__init__("Villager", Alignment.TOWN)

class Nillager(Role):
    def __init__(self):
        super().__init_("Nillager", Alignment.MAFIA)
        self.__actions[Phase.NIGHT] = NormalNightKill