from internal import NamedEntity
from roles import *
from actions import *
from items import *

class Player(NamedEntity):

    def __init__(self, username):
        super().__init__(username)
        self.__is_alive = True
        self.__character = None
        self.__inventory = List[Item]

    def get_character(self) -> Role:
        return self.__character

    def set_character(self, char: Role):
        self.__character = char

    def get_actions(self, phase: Phase) -> List[Action]:
        if not self.__is_alive:
            return List[Action]
        return self.get_character().get_actions(phase)