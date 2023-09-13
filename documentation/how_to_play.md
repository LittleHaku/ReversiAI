# How to play

## How to run the game

- Enter the directory `cd ReversiAI`
- Run the game with `make play`

## Reversi Rules

- The game is played on an 8x8 board
- The game starts with two black and two white pieces in the middle of the board in a cross pattern
- The players take turns placing their pieces on the board
- A player must place their piece on a cell that is adjacent to an opponent's piece and that makes a straight line (horizontal, vertical or diagonal) with another piece of the same color with one or more opponent's pieces between them.
- Then the pieces of the opposite color that are between the one that was just placed and the other piece of the same color are flipped, so you won all those pieces.
- If you can't make a valid move, you pass your turn.
- The game ends when the board is full or when both players can't make a valid move.
- The player with the most pieces of their color on the board wins.
