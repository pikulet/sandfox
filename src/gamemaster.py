'''
The all-seeing gamemaster that holds global variables
'''

from itertools import cycle
from typing import Dict, List

from src.actions import *
from src.voting import DAY_ELIMINATION_VOTING_BOARD, VotingBoard
from player import Player

class GameMaster:

    def __init__(self, players: List[Player]):
        self.__players = dict(map(lambda p: p.get_name(), p, players))
        self.__day = 0
        self.__phase = cycle(Phase.NIGHT, Phase.DAY)
        self.__voting_boards = dict()
        self.__add_voting_board(DAY_ELIMINATION_VOTING_BOARD, players)

    def change_phase(self):
        phase = self.__phase.next()
        if phase == Phase.DAY:
            self.__day += 1
        return self.__day, phase

    def get_state(self):
        return self.__day, self.__phase

    def __add_voting_board(self, board_name: str, players: List[Player]):
        self.__voting_boards[board_name] = VotingBoard(players)

    def get_all_actions(self) -> Dict[str, List[Action]]:
        result = dict()

        for player in self.__players:
            result[player.get_name()] = player.get_actions[self.__phase]

        return result

    def set_action_target(self, player, action, target):
        pass

    def resolve_all_actions(self):
        pass

    def kill_player(self, player_name: str):
        self.__players


