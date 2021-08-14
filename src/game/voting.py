MAFIA_KILL_VOTING_BOARD = "VotingBoard_MafiaKill"
DAY_ELIMINATION_VOTING_BOARD = "VotingBoard_DayElimination"

class VotingException(Exception):
    pass

class VotingBoard:

    def __init__(self, players):
        self.__player_votes = dict.fromkeys(players, None)

    def get_votes(self):
        return self.__player_votes

    def set_vote(self, player, target) -> str:
        """
        Lets player vote for target.
        Returns the vote result (if any), else None
        """

        if player not in self.__player_votes:
            raise VotingException("Player %s is not allowed to vote" % player)
        elif self.__player_votes[player] == target:
            # voting for the same person
            pass

        self.__player_votes[player] = target
        return self.__tally_votes()

    def remove_player(self, player) -> str:
        """
        Removes a player from the voting board.
        Returns the vote result (if any), else None
        """

        del self.__player_votes[player]
        return self.__tally_votes()

    def __tally_votes(self) -> str:
        """
        it's slow to always go through the whole voting chart
        add aux structures like unvoted players and a live tally count?
        """
        return None