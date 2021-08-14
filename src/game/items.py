from typing import Callable


class Item(Action):
    """
    Items are Actions that can be transferred to another Player
    """

    def __init__(self, name, function: Callable[[Player], None]):
        super().__init__(name, function)

class Knife(Item):

    def __init__(self):
        super().__init__("Knife", lambda player: player.die())