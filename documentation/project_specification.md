# Project Specification

This is the project specification for the course TKT20010 at the University of Helsinki in which I'm participating as a Master's student in Computer Science.

The language used in this project will be **English**, and the programming language will be **Python**.

## Project Description

The aim of this project is to create an artificial intelligence that will play Reversi (also known as Othello) against a human player or another AI. This AI will be implemented using the minimax algorithm with alphabeta pruning. To calculate the value of each node, heuristics which take into account the state of the game and give a value of how good or bad would a certain move be will be used, then each of the heuristics will have a different weight and the final value of the node will be calculated as a weighted sum of the heuristics.

## Data Structures and Algorithms

For algorithms I will be using minimax with alphabeta pruning, since its an algorithm that is highly used in game theory, it analyzes all the possible moves until a certain depth and then chooses the best one.

The program won't be using any complex data structures, just the basic ones that Python provides, such as lists, dictionaries, etc. In addition to that numpy will be used to represent the board as a matrix between other things.

## Input and Output

### Terminal

The program will be executed from a terminal, the output here will be an ASCII representation of the board, and also the number of coins/tokens that each player currently has. There will be a verbose level that will show the AI's node evaluations that willl be helpful for debugging and comparing the performance of different heuristics and weight combinations.

### GUI

The program's GUI inputs will be the player's moves in case of playing human against AI, or human versus human, and the outputs will be the AI's moves.

## Time and Space Complexity

The time complexity of minimax with alphabeta pruning is $O(b^d)$ in the worst case (there was no pruning) with its best case being $O(b^{d/2})$, where b is the branching factor and d is the depth of the tree. In this case the branching factor is not known since the number of possible moves depends on the current state of the game and it could even be 0. The depth of the tree will allowed to be changed in the code to test how well the AI performs with different depths without sacrificing too much the performance.

The space complexity of minimax with alphabeta pruning is $O(b \cdot d)$ since in the worst case that it had to explore all the nodes, it would need to store all of them $(b \cdot d)$.
