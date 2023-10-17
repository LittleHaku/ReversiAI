# Implementation

## Project Structure

The project is made of one package, `reversi`, this module contains three files:

- `reversi_logic.py`: Contains the game logic and the AI implementation, this means it contains how the game is initialized, decides if a piece can be placed in a certain cell, flips the pieces when a piece is placed, decides if a player can make a move, decides if the game has ended, etc. And also has the AI implementation, which is a minimax with alphabeta pruning and different heuristics.
- `reversi_gui.py`: Contains the GUI implementation, this means it contains the code to draw the board, the pieces, the menu, the buttons, etc.
- `main.py`: Contains the main function, simply creates a Tkinter window and runs the game.

## Time and Space Complexity

### Time Complexity

The time complexity of the minimax algorithm is `O(b^m)`, where `b` is the branching factor and `m` is the maximum depth of the tree. In this case the branching factor is 8, since there are 8 possible directions to place a piece, and the maximum depth is 64, since the board is 8x8. This means that the time complexity of the minimax algorithm is `O(8^64)`, which is a very big number, so it is not possible to calculate the exact time complexity of the algorithm. However, since the algorithm uses alphabeta pruning, the time complexity is reduced to `O(b^(m/2))`, which is `O(8^32)`, which is still a very big number, but it is a lot smaller than `O(8^64)`.

The time complexity of this program is mainly determined by the minimax algorithm which has a time complexity of $O(b^d)$ where $b$ is the branching factor and $d$ is the maximum depth of the tree, in the Reversi (Othello) game it is estimated that on average 10 different moves can be made during each player's turn, this would be our $b$, then the average game lasts 58 moves, this would be our $d$, so the time complexity of the minimax algorithm would be $O(10^{58})$ [1], since we use alpha-beta pruning on the best case we will get a time complexity of $O(10^{29})$, while the worst one will still be $O(10^{58})$ [2].

### Space Complexity

## References

[1]: http://fragrieu.free.fr/SearchingForSolutions.pdf
[2]: https://www.codingninjas.com/studio/library/the-alpha-beta-pruning-algorithm
