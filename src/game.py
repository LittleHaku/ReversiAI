"""
Basics for a game with two players.
"""


class Player(object):
    """A player in a two-player game."""

    def __init__(
        self,
        name: str,  # Name of the player
        strategy: "Strategy",  # Strategy of the player
        delay: int = 0,  # Delay before the player moves
    ) -> None:
        self.label: Any = None
        self.name = name
        self.strategy = strategy
        self.delay = delay

    def move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Player's move."""
        if self.delay > 0:
            time.sleep(self.delay)
        return self.strategy.next_move(state, gui)
