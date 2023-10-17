# How to play

## Installation

- Clone the repository
- Install poetry with `curl -sSL https://install.python-poetry.org | python3 -` or `make install_poetry`

## How to run the game

- Enter the directory `cd ReversiAI`
- Run the game with `make play`
- In the menu below select if you want to play with blacks or whites
- If you want to restart the game you can always do so with the button below and selecting the pieces you want to play with again
  
## Modifying Playing Time of the AI

If you want to make the AI take longer or shorter, this can be done in the file [reversi_logic.py](/src/reversi/reversi_logic.py) and modify `self.max_time` to be equal to the number of seconds you want to take. Higher times will have a deeper minimax and thus the AI will be better, I recommend setting it to 1.

## Reversi Rules

- The game is played on an 8x8 board
- The game starts with two black and two white pieces in the middle of the board in a cross pattern
- The players take turns placing their pieces on the board
- A player must place their piece on a cell that is adjacent to an opponent's piece and that makes a straight line (horizontal, vertical or diagonal) with another piece of the same color with one or more opponent's pieces between them.
- Then the pieces of the opposite color that are between the one that was just placed and the other piece of the same color are flipped, so you won all those pieces.
- If you can't make a valid move, you pass your turn.
- The game ends when the board is full or when both players can't make a valid move.
- The player with the most pieces of their color on the board wins.
