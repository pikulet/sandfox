from enum import Enum
from typing import Callable

from internal.internal import NamedEntity
from player import Player

class Action(NamedEntity):
    """
    Actions can be done by Characters, on Players
    """

    def __init__(self, name: str, phase: Phase, function: Callable[[Player], None]):
        super().__init__(name)
        self.__phase = phase
        self.__function = function
        self.__target = None

    def set_target(self, target: Player):
        self.__target = target

    def resolve(self):
        # check global phase first
        self.__function(self.__target)

class DayEliminationVote(Action):
    def __init__(self):
        vote_function = lambda player: None
        super().__init__("DayEliminationVote", Phase.DAY, vote_function)

class NormalNightKill(Action):
    def __init__(self):
        kill_action = lambda player: None
        super().__init__("NormalNightKill", Phase.NIGHT, kill_action)

class GiveItem(Action):
    def __init__(self):
        give_action = lambda player: player.