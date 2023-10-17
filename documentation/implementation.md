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

In the program these depths are not reached since if not the game would be too slow, so the time complexity is closer to a depth of 3 to 7, depends on the time we allow the AI to think, but we could say that the time complexity is $O(10^7)$.

### Space Complexity

The space complexity when using minimax is $O(bd)$ even when using alpha-beta pruning [3], as previously stated our $b$ will be 10 and our $d$ will be 58, so the space complexity will be $O(10*58)$.

As it was stated in the time complexity, these depths are not reached since the game uses a timer to limit the time the AI can take on each move, so the space complexity is closer to $O(10*7)$.

## Possible Improvements

### Better Heuristics with Machine Learning

The heuristics that I have used are the most commonly used [4], [5]. How ever better heuristics can be found and machine learning can be used to find the closest weights to the optimal ones.

### Cache (memoization)

Although I have implemented a cache, my implementation is not the best since it uses the whole board as a key for a dictionary and this is not very efficient, so other cache implementations could be more efficient and thus help the minimax to reach higher depths in less time.

## References

[1]: http://fragrieu.free.fr/SearchingForSolutions.pdf
[2]: https://www.codingninjas.com/studio/library/the-alpha-beta-pruning-algorithm
[3]: https://ai-master.gitbooks.io/adversarial-search/content/property-of-alpha-beta-pruning-algorithm.html
[4]: https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/
[5]: https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf

1. [Searching for Solutions](http://fragrieu.free.fr/SearchingForSolutions.pdf)
2. [The Alpha-Beta Pruning Algorithm](https://www.codingninjas.com/studio/library/the-alpha-beta-pruning-algorithm)
3. [Property of Alpha-Beta Pruning Algorithm](https://ai-master.gitbooks.io/adversarial-search/content/property-of-alpha-beta-pruning-algorithm.html)
4. [Heuristic Function for Reversi/Othello](https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/)
5. [Heuristics in Othello](https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf)
